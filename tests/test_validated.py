import re
from dataclasses import dataclass
from pytypus.either import cond
from pytypus.validated import Validated, from_either, validate
from pytypus.list import Chain


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
    def error_message(self) -> str:
        raise NotImplementedError()


class UsernameHasSpecialCharacters(DomainValidation):
    @property
    def error_message(self) -> str:
        return "Username cannot contain special characters."


class PasswordTooShort(DomainValidation):
    @property
    def errorMessage(self) -> str:
        return "Password must be at least 8 characters long"


class RegistrationFormValidator(object):

    def validate_username(self, username: str) -> Validated[DomainValidation, str]:
        match = re.findall(r"(?:^|(?<=\s))", username, flags=re.IGNORECASE)
        return from_either(cond(len(match) > 0, username, UsernameHasSpecialCharacters()))

    def validate_password(self, password: str) -> Validated[DomainValidation, str]:
        return from_either(cond(len(password) > 8, password, UsernameHasSpecialCharacters()))

    def validateForm(self, username: str, password: str, first_name: str, last_name: str, age: int) -> Validated[Chain[DomainValidation], RegistrationData]:
        validation_result: Chain[Validated[DomainValidation, str]] = Chain([
            self.validate_username(username),
            self.validate_password(password)])
        return validate(validation_result, RegistrationData(username, password, first_name, last_name, age))


def test_validation() -> None:
    result = RegistrationFormValidator().validateForm(
        "don", "chuck", "Beaver", "Don", 75)
    assert result
