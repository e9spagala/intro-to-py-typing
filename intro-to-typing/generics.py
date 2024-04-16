from typing import TypeVar, List 

'''
Generic type is a place holder type.
It is used when you dont know what kind of the 
type is going to be used.
'''
T = TypeVar('T')

def get_item(lst: List[T], ind: int) -> T:
    return lst[ind]