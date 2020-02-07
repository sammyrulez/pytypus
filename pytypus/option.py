from __future__ import annotations
from pytypus.functor import Functor
from typing import Generic, Iterable, Optional, TypeVar, Union, Callable


T = TypeVar('T')
S = TypeVar('S')


class OptionT(Functor[T]):

    def __init__(self, v: Union[T, None]) -> None:
        self._value = v

    def map(self, f: Callable[[T], S]) -> OptionT[S]:
        if(self._value):
            return OptionT(f(self._value))
        else:
            return OptionT(None)

    def flat_map(self, f: Callable[[T], OptionT[S]]) -> OptionT[S]:
        if(self._value):
            return f(self._value)
        else:
            return OptionT(None)

    def is_empty(self):
        return self._value is None

    def or_value(self, v: T) -> T:
        if(self._value):
            return self._value
        else:
            return v

    def or_rise(self, e: RuntimeError) -> T:
        if(self._value):
            return self._value
        else:
            raise e

    def or_else(self, v: T) -> OptionT[T]:
        if(self._value):
            return self
        else:
            return OptionT(v)

    def to_Optional(self) -> Optional[T]:
        return self._value

    def __str__(self) -> str:
        if(self._value):
            return str(self._value)
        else:
            return "EmptyOption"

    def __eq__(self, o: object) -> bool:
        if(self._value):
            return self._value == o
        else:
            return False

    def __sizeof__(self) -> int:
        if(self._value):
            return 1
        else:
            return 0

    def __iter__(self) -> Iterable[T]:
        if(self._value):
            return iter(self._value)
        else:
            return iter([])


def empty() -> OptionT[any]:
    return OptionT(None)  # type: ignore


def some(v):
    return OptionT(v)


def from_optional(v: Optional[any]) -> OptionT[any]:
    return OptionT(v)  # type: ignore
