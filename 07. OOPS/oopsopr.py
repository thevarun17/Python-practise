
class parentclass1:

    def divn(self):
        res = self.a / self.b
        return res

    def test1(self):
        return "test1func"

    def test2(self):
        return "rama"


class parentclass2:
    def evenorodd(self):
        return self.a % 2

    def rohit(self):
        return "all the best rohit"



class childclass(parentclass1,parentclass2):
    #parent functions will be coming first and then child funcs
    def __init__(self,a,b,c,d,e,f):
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

    def mod(l,m):
        res = l  % m
        return res


    def test2(self):
        return "santhosh"


obj1 = childclass(50,20,30,60,20,10)
obj2 = childclass(5,2,7,8,3,1)
obj3 = childclass(100,200,400,300,50,70)

# print(obj1.a)
# print(obj2.c)
# print(obj3.f)

# res = childclass.addn(obj3)
# print(res)
#
# res = childclass.subn(obj2)
# print(res)
#
# res = childclass.test2(obj1)
# print(res)
#
# res = childclass.mod(30,7)
# print(res)


### Inheritance

# res = childclass.divn(obj1)
# print(res)
#
# res = childclass.evenorodd(obj3)
# print(res)



## overwriting

res = childclass.test2(obj1)
print(res)


### overloading

res = parentclass1.test2(obj1)
print(res)