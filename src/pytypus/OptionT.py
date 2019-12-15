from typing import Generic, TypeVar, Union, Callable


T = TypeVar('T')
S = TypeVar('S')

class OptionT(Generic[T]):

    value : Union[T, None] 

    def __init__(self,v: Union[T, None]) -> None:
        self.value = v

    def map(self, f:Callable[[T],S]) -> Union[S, None]:
        if(self.value):
            return  OptionT(f(self.value))
        else:   
            return OptionT(None)


        
