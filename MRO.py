class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # D inherits from B and C
    pass

d = D()
d.show()  # Output: B (because B comes first in MRO)

# View MRO
print(D.__mro__)
