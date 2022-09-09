class Human:
    count = 0
    leg = 0

    def __init__(self, name="", age=0):
        self._name = name
        self._age = age

        Human.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_minor(age):
        return age < 16

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        # print("Calling the setter")
        if name.islower():
            raise ValueError("Name cannot be all lower case")
        self._name = name

    @name.deleter
    def name(self):
        # print("Deleting ...")
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: str):
        # print("calling age setter")
        self._age = age

    @age.deleter
    def age(self):
        print("Deleting age")
        del self._age


Man = Human()
Man.name = "Ibrahim"
Man.age = 34

print(f"This is name for the first man object {Man.name} and age is {Man.age}")

Man.name = "Judith"
Man.age = 4

print(f"This is the second man object name: {Man.name} and age is {Man.age}")

Man.name = "Joanna"
Man.age = 1

print(f"This is the third man object name: {Man.name} and age is {Man.age}")

print(Man.is_minor(78))
