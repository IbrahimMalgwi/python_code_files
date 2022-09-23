import abc


class Mammal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def move(self):
        pass


m1 = Mammal()
