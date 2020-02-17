from __future__ import annotations
from typing import List, TypeVar, Generic, Callable

T = TypeVar('T')
S = TypeVar('S')


class Chain(Generic[T]):

    list: List[T]

    def __init__(self,  list: List[T]):
        self.list = list

    def map(self, f: Callable[[T], S]) -> Chain[S]:
        return Chain(map(f, self.list))

    def flat_map(self, f: Callable[[T], Chain[S]]) -> Chain[S]:
        temp: List[S] = []
        for e in list:
            temp = temp + f(e)
        return Chain(temp)

    def filter(self, f: Callable[T, bool]) -> Chain[T]:
        temp: List[T] = []
        for e in self.list:
            if f(e):
                temp.append(e)
        return Chain(temp)

    def __sizeof__(self):
        return len(self.list)
