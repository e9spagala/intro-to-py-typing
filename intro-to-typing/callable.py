from typing import Callable
'''
Callable is used when a function is accepted as a param
'''

def foo(func: Callable[[int, int], int]) -> int:
    return func(1, 2)
    
def add(a:int, b:int) -> int:
    return a + b

# return a function

def return_function() -> Callable[[int, int], int]:
    def add(a: int, b: int) -> int:
        return a + b
    return add
