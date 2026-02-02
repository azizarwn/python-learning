from pydantic import BaseModel

students: list[dict[str, str | int, bool]] = [{
    "name": "John",
    "age": 20,
    "city": True,
    "is_student": True
}]

name: str = 23

def sum(a: int, b: int) -> int:
    return a + b

sum_result: int = sum(1, 2)


# list of string, can be mixed with different types
fruits: list[str] = ["apple", "banana", "cherry"]

user: dict[str, str] = {"name": "John", "age": "20"}

# union, can be int or str
data: int | str = 1
data_a: int | None = None # None is a special type that means no value


# untuk buat shape of data 
class User(BaseModel):
    name: str
    age: int

user = User(name="John", age=20)
print(user.name)
print(user.age)
print(user.model_dump()) # untuk convert data ke dict
