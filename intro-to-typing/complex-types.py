from typing import List, Optional, Any, Sequence
'''
define type in a variable. Follow the convention
that the first letter of the type should be capital
''' 
Vector = List[float]

def foo(v: Vector) -> Vector:
    return v

'''
correct way of specifing optional params. 
It won't give any errors if it is not done like this
but its a best practice
'''

def default_param(val: Optional[int]=0) -> Optional[int]:
    return val

# any type

def any_param(val: Any) -> None:
    print(val)

'''
If you are not sure about the type 
of the sequential data structure provided in the input
you can use Sequence type

It will accept string(only if the type of the seuqence is a string), tuple and list
set is not considered as a sequence as it is unordered.
'''
def sequences(arr: Sequence[str]) -> Sequence[str]:
    return arr

arr = sequences(['1', '2', '4'])
arr = sequences(('1', '2', '4'))
arr = sequences("hello world")



