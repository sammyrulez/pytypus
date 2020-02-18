from typing import TypeVar, Generic
from pytypus.either import Either, cond
from pytypus.list import Chain

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


def from_either(e: Either[E, A]) -> Validated[E, A]:
    if(e.left):
        return InValid(e.left)
    else:
        return Valid(e.right)


def validate(validator_chain: Chain[E], output: A) -> Validated[Chain[E], A]:
    return from_either(cond(validator_chain.filter(lambda e: isinstance(e, Valid)), validator_chain, output))
