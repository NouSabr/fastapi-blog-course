# From python 3.10 onwards, no need to import typing

from typing import List, Optional

x: List[int | float] = [1.2, 4, 5, 6.7]

# We can use classes as typehints

class Job:
    def __init__(self, title: str, description: Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title
    

job1 = Job(title= "Team Lead", description= "Lorem ipsum")
job2 = Job(title= "Senior Manager", description= "dolor sit amet")

jobs = List[Job]

from typing import Callable

#the Callable type is for functions. the first argument(list) are the arguments of the method, the second is the return.
def smart_divide(func: Callable[[int, int], float]):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)  
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(9, 0)
    