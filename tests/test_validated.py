from pytypus.either import Either, cond
from pytypus.validated import Valid, Validated, from_Either, validate
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


class PasswordTooShort(DomainValidation):
    @property
    def errorMessage(self) -> str:
        return "Password must be at least 8 characters long"


class RegistrationFormValidator(object):

    def validate_username(self, username: str) -> Validated[DomainValidation, str]:
        match = re.findall(r"(?:^|(?<=\s))", username, flags=re.IGNORECASE)
        return from_Either(cond(match, username, UsernameHasSpecialCharacters))

    def validate_password(self, password: str) -> Validated[DomainValidation, str]:
        return from_Either(cond(len(password) > 8, password, UsernameHasSpecialCharacters))

    def validateForm(self, username: str, password: str, first_name: str, last_name: str, age: int) -> Validated[Chain[DomainValidation], RegistrationData]:
        validationResult = Chain([
            self.validate_username(username),
            self.validate_password(password)])
        return validate(validationResult, RegistrationData(username, password, first_name, last_name, age))


def test_validation():
    result = RegistrationFormValidator().validateForm(
        "don", "chuck", "Beaver", "Don", 75)
    assert result
