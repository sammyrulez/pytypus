from __future__ import annotations
from typing import List, TypeVar, Generic, Callable
from copy import copy

T = TypeVar('T')
S = TypeVar('S')


class Chain(Generic[T]):

    _inner_list: List[T]

    def __init__(self, my_list: List[T]):
        self.list = my_list

    def map(self, f: Callable[[T], S]) -> Chain[S]:
        return Chain(list(map(f, self._inner_list)))

    def flat_map(self, f: Callable[[T], Chain[S]]) -> Chain[S]:
        temp: List[S] = []
        for e in self._inner_list:
            temp = temp + f(e).as_list()
        return Chain(temp)

    def filter(self, f: Callable[[T], bool]) -> Chain[T]:
        temp: List[T] = []
        for e in self._inner_list:
            if f(e):
                temp.append(e)
        return Chain(temp)

    def as_list(self) -> List[T]:
        return copy(self._inner_list)

    def __sizeof__(self) -> int:
        return len(self._inner_list)

    def __bool__(self) -> bool:
        return len(self._inner_list) > 0
