from __future__ import annotations
from pytypus.option import OptionT, some, empty
from pytypus.functor import Functor
from typing import Generic, Iterable, Optional, TypeVar, Union, Callable

L = TypeVar("L")
R = TypeVar("R")
S = TypeVar("S")


class Either(Generic[L, R], Functor[R]):

    def __init__(self, left: L = None, right: R = None) -> None:
        if left == None and right == None:
            raise RuntimeError("'right' and 'left' can not be both None")
        if left != None and right != None:
            raise RuntimeError("'right' and 'left' can not be both defined")
        self._left = left
        self._right = right

    def map(self, f: Callable[[R], S]) -> Either[L, S]:
        if self._right != None:
            return Either(right=f(self._right))
        else:
            return self

    @property
    def left(self) -> L:
        return self._left

    @property
    def right(self) -> R:
        return self._right

    def as_optional(self) -> Optional[R]:
        return self._right

    def as_option_t(self) -> OptionT[R]:
        if self._right:
            return some(self._right)
        else:
            return empty()

    def __str__(self) -> str:
        if(self._right):
            return str(self._right)
        else:
            return "left(%s)" % str(self.left)

    def __eq__(self, o: object) -> bool:
        if(self._right):
            return self._right == o
        else:
            return self._left == o  # TODO check if o is a either

    def __sizeof__(self) -> int:
        if(self._right):
            return 1
        else:
            return 0

    def __iter__(self) -> Iterable[R]:
        if(self._right):
            return iter(self._right)
        else:
            return iter([])


def left(l: L) -> Either[L, R]:
    return Either(left=l)


def right(r: R) -> Either[L, R]:
    return Either(right=r)


def cond(condition: bool, r: R, l: L) -> Either[L, R]:
    if condition:
        return right(r)
    else:
        return left(l)
