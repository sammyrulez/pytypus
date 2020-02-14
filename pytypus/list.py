from typing import List, TypeVar, Generic

T = TypeVar('T')
S = TypeVar('S')


class Chain(Generic[T]):

    list: List[T]

    def __init__(self,  list: List[T]):
        self.list = list

    def map(self, f: Callable[[T], S]) -> Chain[S]:
        return Chain(map(f, self.list))

    def flat_map(self, f: Callable[[T], Chain[S]]) -> Chain[S]:
        temp: List[T] = []
        for e in list:
            temp = temp + f(e)
        return Chain(temp)
