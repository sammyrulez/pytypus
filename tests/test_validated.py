from pytypus.either import Either, cond
from pytypus.validated import Valid, Validated, from_Either
from pytypus.list import Chain
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

    def validateForm(self, username: str, password: str, first_name: str, last_name: str, age: int) -> Validated[Chain[DomainValidation], RegistrationData]:
        """  for { 
            validatedUserName <- validateUserName(username)
            validatedPassword <- validatePassword(password)
            validatedFirstName <- validateFirstName(firstName)
            validatedLastName <- validateLastName(lastName)
            validatedAge <- validateAge(age)
        } yield RegistrationData(validatedUserName, validatedPassword, validatedFirstName, validatedLastName, validatedAge)
        """
        validationResult = Chain([self.validateUsername(
            username), password, first_name, last_name, age])

        return from_Either(cond(validationResult.filter(lambda e: isinstance(e, Valid)), validationResult, RegistrationData(username, password, first_name, last_name, age)))


def test_validation():
    result = RegistrationFormValidator().validateForm(
        "don", "chuck", "Beaver", "Don", 75)
    assert result
