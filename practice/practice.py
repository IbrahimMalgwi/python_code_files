class Practice:
    count = 0

    def __int__(self, first):
        self.first = first

    def play(self):
        return f"playing with {self.first}"

    @classmethod
    def create(cls, name):
        return cls(name)

    @staticmethod
    def just_here():
        return "Just hanging out here!!!"


p1 = Practice("Banke")
p2 = Practice.create("Hadiza")