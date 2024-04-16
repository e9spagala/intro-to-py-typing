
from typing import Dict, List, Set, Union
#returns number
def add_numbers(a:int, b: int, c:int) ->  int:
    return a + b + c


# returns void
def return_sum(a:int, b: int, c:int) -> None:
    print(a + b + c)
# list
lst: List[int] = [1, 32, 23]
multi_lst: List[Union[str, int]] = [1, 32, 23, 'sai', 'mayur', 'anuradha']


# dict type
memo: Dict[str, str] = {'a': 'hellow'}
non_dupe: Set[int] = {1, 2}

