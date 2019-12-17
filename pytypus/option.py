from __future__ import annotations
from typing import Generic, TypeVar, Union, Callable


T = TypeVar('T')
S = TypeVar('S')


class OptionT(Generic[T]):

    def __init__(self, v: Union[T, None]) -> None:
        self.value = v

    def map(self, f: Callable[[T], S]) -> OptionT[S]:
        if(self.value):
            return OptionT(f(self.value))
        else:
            return OptionT(None)

    def flatMap(self, f: Callable[[T], OptionT[S]]) -> OptionT[S]:
        if(self.value):
            return f(self.value)
        else:
            return OptionT(None)

    def is_empty(self):
        return self.value is None


def empty() -> OptionT[any]:
    return OptionT(None)


def some(v):
    return OptionT(v)
