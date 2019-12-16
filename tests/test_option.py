from __future__ import annotations
from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")
S = TypeVar("S")


class Functor(Generic[T]):
    def map(self, function: Callable[[T], S]) -> Functor[S]:
        raise NotImplementedError


def test_map():
    from pytypus import option
    e = option.empty()
    mapped_e = e.map(lambda k: str(k))
    assert mapped_e.is_empty() == True
