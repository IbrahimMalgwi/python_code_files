from dataclasses import dataclass, field


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

@dataclass(order=True)
class Person:
    sort_with: tuple = field(init=False, repr=False)
    age: int
    name: str
    height: int = field(default=0)

    def __post_init__(self):
        self.sort_with = (self.height, self.age)

    def get_age(self):
        return self.age


p1 = Person(name="Judith", age=35)
p2 = Person(name="Joanna", age=45)
p3 = Person(name="Victor", age=20)
print(p1 < p2)
