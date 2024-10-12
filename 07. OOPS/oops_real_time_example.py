class ParentClass1:
    def divn(self):
        res = self.a / self.b
        return res

    def test1(self):
        return "test1func"

    def test2(self):
        return "rama"


class ParentClass2:
    def evenorodd(self):
        return self.a % 2

    def rohit(self):
        return "all the best rohit"


class ChildClass(ParentClass1, ParentClass2):
    # Parent functions will be coming first and then child functions
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def addn(self):
        res = self.a + self.b + self.c
        return res

    def subn(self):
        res = self.d - self.e - self.f
        return res

    def mul(self):
        res = self.a * self.c
        return res

    @staticmethod
    def mod(l, m):  # Changed to static method
        res = l % m
        return res

    def test2(self):  # Overriding the parent class method
        return "santhosh"


# Creating instances of ChildClass
obj1 = ChildClass(50, 20, 30, 60, 20, 10)
obj2 = ChildClass(5, 2, 7, 8, 3, 1)
obj3 = ChildClass(100, 200, 400, 300, 50, 70)

# Accessing attributes
print(obj1.a)  # Output: 50
print(obj2.c)  # Output: 7
print(obj3.f)  # Output: 70

# Using methods from ChildClass
res = obj1.addn()  # Call addn on obj1
print("Addition Result (obj1):", res)  # Output: Addition Result (obj1): 100

res = obj2.subn()  # Call subn on obj2
print("Subtraction Result (obj2):", res)  # Output: Subtraction Result (obj2): 4

res = obj1.test2()  # Call overridden test2 on obj1
print("Test2 Result (obj1):", res)  # Output: Test2 Result (obj1): santhosh

res = ChildClass.mod(30, 7)  # Call static method mod on ChildClass
print("Modulus Result:", res)  # Output: Modulus Result: 2

# Using methods from parent classes through an instance of ChildClass
res = obj1.divn()  # Call divn from ParentClass1 using obj1
print("Division Result (obj1):", res)  # Output: Division Result (obj1): 2.5

res = obj3.evenorodd()  # Call evenorodd from ParentClass2 using obj3
print("Even or Odd (obj3):", res)  # Output: Even or Odd (obj3): 0 (100 is even)