
from __future__ import annotations
from typing import Generic, TypeVar, Callable

T = TypeVar("T")
S = TypeVar("S")


class Functor(Generic[T]):
    def map(self, function: Callable[[T], S]) -> Functor[S]:
        raise NotImplementedError
