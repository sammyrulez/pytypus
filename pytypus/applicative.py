from typing import Generic, TypeVar, Callable

from .functor import Functor

T = TypeVar("T")
A = TypeVar("A")
B = TypeVar("B")


class Applicative(Functor[T]):
    def product(self, fa: Callable[[A], T], fb: Callable[[B], T]) -> Callable[[T], (A, B)]:
        raise NotImplementedError

    def map2(self, mf: Callable[[A, B]], T) -> Functor[T]:
        raise NotImplementedError

 # def pure[A](a: A): F[A]
