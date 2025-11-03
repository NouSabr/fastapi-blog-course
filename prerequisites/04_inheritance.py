# class Python:
#     def __init__(self) -> None:
#         self.is_cool = True

# class FastAPI(Python):
#     pass

# f = FastAPI()
# print(f.is_cool)

class Pydantic:
    def is_valid(self, text: str) -> bool:
        if "admin" in text:
            return False
        return True
    

class Starlette:
    def is_valid(self, text: str) -> bool:
        return True
    

class FastAPI(Pydantic, Starlette):
    pass

f = FastAPI()

# __mro__ stands for Method Resolution Order. 
# It returns a list of types the class is derived from, in the order they are searched for methods.
print(FastAPI.__mro__)
print(f.is_valid("admin tried to sign in"))