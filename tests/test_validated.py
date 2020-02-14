from pytypus.either import Either, cond


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
        cond(False, username, UsernameHasSpecialCharacters)
