from pytypus.either import Either, cond
from pytypus.validated import Validated, from_Either
from dataclasses import dataclass


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
        return from_Either(cond(True, username, UsernameHasSpecialCharacters))

    def validateForm(self, username: str, password: str, firstName: str, lastName: str, age: int) -> Validated[DomainValidation, RegistrationData]:
        """  for { 
            validatedUserName <- validateUserName(username)
            validatedPassword <- validatePassword(password)
            validatedFirstName <- validateFirstName(firstName)
            validatedLastName <- validateLastName(lastName)
            validatedAge <- validateAge(age)
        } yield RegistrationData(validatedUserName, validatedPassword, validatedFirstName, validatedLastName, validatedAge)
        """
        validated = self.validateUsername(username)
        return validated


def test_validation():
    result = RegistrationFormValidator().validateForm(
        "don", "chuck", "Beaver", "Don", 75)
    assert result
