
from typing import TypeVar, Generic
from pytypus.either import Either

E = TypeVar("E")
A = TypeVar("A")


class Validated(Generic[E, A]):
    pass


class Valid(Validated[None, A]):
    a: A

    def __init__(self, a: A):
        super().__init__()
        self.a = a


class InValid(Validated[E, None]):
    e: E

    def __init__(self, e: E):
        super().__init__()
        self.e = e


def from_Either(e: Either[E, A]) -> Validated[E, A]:
    if(e.left):
        return InValid(e.left)
    if(e.right):
        return Valid(e.right)
