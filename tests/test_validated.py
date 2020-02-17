from pytypus.either import Either, cond
from pytypus.validated import Valid, Validated, from_Either
from pytypus.list import Chain
from dataclasses import dataclass
import re


@dataclass
class RegistrationData:
    username: str
    password: str
    firstName: str
    lastName: str
    age: int


@dataclass
class DomainValidation:
    @property
    def errorMessage(self) -> str:
        raise NotImplementedError()


class UsernameHasSpecialCharacters(DomainValidation):
    @property
    def errorMessage(self) -> str:
        return "Username cannot contain special characters."


class RegistrationFormValidator(object):

    def validateUsername(self, username: str) -> Validated[DomainValidation, str]:
        match = re.findall(r"(?:^|(?<=\s))", username, flags=re.IGNORECASE)
        return from_Either(cond(match, username, UsernameHasSpecialCharacters))

    def validateForm(self, username: str, password: str, first_name: str, last_name: str, age: int) -> Validated[Chain[DomainValidation], RegistrationData]:
        validationResult = Chain([
            self.validateUsername(username),
            password, first_name, last_name, age])

        return from_Either(cond(validationResult.filter(lambda e: isinstance(e, Valid)), validationResult, RegistrationData(username, password, first_name, last_name, age)))


def test_validation():
    result = RegistrationFormValidator().validateForm(
        "don", "chuck", "Beaver", "Don", 75)
    assert result
