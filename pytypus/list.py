from typing import List, TypeVar, Generic

T = TypeVar('T')
S = TypeVar('S')


class Chain(Generic[T]):

    list: List[T]

    def map(self, f: Callable[[T], S]) -> Chain[S]:
        pass

    def flat_map(self, f: Callable[[T], Chain[S]]) -> Chain[S]:
        pass
