# #creating class
# class Student:
#     name = "Varun kumar"
#     #creating objects
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)
#
#
# class Car:
#     color = 'blue'
#     brand = 'mercedes'
# car1 = Car()
# print(car1.color)
# print(car1.brand)


# class Student:
#     name = 'karnam'
#
#     # init method or constructor
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("Adding new students")
# s1= Student("karan",90)
# print(s1.name,s1.marks)
# s2 = Student("varun",98)
# print(s2.name,s2.marks)

#attributes
# mini project for creating bank account deduction
class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs:", amount, 'was debited from your account')
        print("Total balance=", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS:", amount, "was credited into your account")
        print("Total balance=", self.get_balance())

    def get_balance(self):
        return self.balance

# Example usage:
acc = account(100000, "1234567890")
acc.credit(10000)
acc.debit(20000)





