
class Address:
    def __int__(self, number, street, city):
        self.number = number
        self.street = street
        self.city = city


class Person:
    def __int__(self, name: str, address: Address):
        self.name = name
        self.address = address


addr = Address(312, "Herbert Macaulay", "Yaba")
p1 = Person("Hadiza", addr)

print(p1.address)