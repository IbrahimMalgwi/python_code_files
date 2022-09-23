class A:
    def do_this(self):
        print("From A")


class B(A):
    pass


class C(A):
    def do_this(self):
        print("From C")


class D(B, C):
    pass


d = D()
d.do_this()

print(D.mro())
print(D.__mro__)
help(D)

