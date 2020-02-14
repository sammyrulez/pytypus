
from typing import TypeVar

E = TypeVar("E")
A = TypeVar("A")


class Validated(Generic[E, A]):
    pass


class Valid(Validated[None, A]):
    a: A


class InValid(Validated[E, None]):
    e: E
