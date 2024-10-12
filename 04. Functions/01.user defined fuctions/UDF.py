# simple function creation

# def test(x,y,z):
#     res = x + y + z
#     return res
# print(test(10,20,30))
#
# op = test(10,10,80) # calling functions with values
# print(op)
#
# op = test(20,5,60)
# print(op)
#
# op = test(1,3,6)
# print(op)





## multiple return values

# def test(x,y,z):
#     res1 = x + y + z
#     res2 = x - y - z
#     res3 = x * y * z
#     return res1 ,res2,res3
# res = []
# op = test(80,10,5)
# for x in op:
#   res.append(x)
# print(op)
# print(res)






### Sample use of function


# def mobval(num):
#     ''' this func is used for mobile number validation '''
#     res1 = len(num)
#     res2 = num.isdigit()
#     if(re s1 == 10 and res2 == True):
#         return "Valid Number"
#     else:
#         return "invalid number"
#
# op = mobval("176171")
# print(op)
# op = mobval("616116")
# print(op)
# op = mobval("9986019197")
# print(op)




# mobile num validation for multiple nums

# def mobval(num):
#     ''' this func is used for mobile number validation '''
#     print(num)
#     res = []
#     for x in num:
#         res1 = len(x)
#         res2 = x.isdigit()
#         if(res1 == 10 and res2 == True):
#             res.append(x)
#         else:
#             res.append("invalid number")
#     return res
#
# op = mobval(['997828', '9980119198', '6363636789' , '14151'])
# print(op)




# mobile num validation for multiple nums in dictionary format

# def mobval(num):
#     ''' this func is used for mobile number validation '''
#     print(num)
#     res = {}
#     for x in num:
#         res1 = len(x)
#         res2 = x.isdigit()
#         if(res1 == 10 and res2 == True):
#             res.setdefault(x,"valid number")
#         else:
#             res.setdefault(x,"invalid number")
#     return res
#
# op = mobval(['997828', '9980119198', '6363636789' , '14151'])
# print(op)
# a=op.values()
# print(a)
# b= op.keys()
# print (b)















#local and global variable concept

# any variable created inside the function is Local Variable
# any variable created outside the function is global Variable

# place = "bangalore"

# def test(x,y,z):
#     global name
#     name = "santhosh"
#     print("Accessing place variable inside function => ", place)
#     print("Accessing name variable inside function => ", name)
#     res = x + y + z
#     return res

# op = test(30,10,5)
# print(op)
# #
# print("Accessing place variable outside function => ", place)
# print("Accessing name variable outside function => ", name)

# Explaining multiple return statements

# def test(x,y,z):
#     res1 = x + y + z
#     res2 = x - y - z
#     res3 = x * y * z
#     return res1 , res2 , res3
#
# op = test(20,10,5)
# print(op)


















# types of UDF

# 1. required and positional arg
#
# def test(x,y,z):
#     res = x + y + z
#     return res
#
# op = test(20,10,5)
# print(op)


# # 2. required and non positional keyword  arg

def test(x,y,z):
    res = x + y
    return res

op = test(y = 'kumar',z = 'yadav', x = 'santhosh')
print(op)


# 3. default arg func

# def test(x=200,y=300,z=500):
#     res = x + y + z
#     return res
# # a =test()
# # print(a)
#
# op = test(100,200,300) # when values are in objects it selects the argument of object only
# print(op)





# # # # 4. variable length arg func
# # Var leng arg shld always be at last

# def test(x,*y):
#     print(x)
#     print(y)
#     # print(z)
#
# test(10,20,30,40,50,60,70)



# multiple Keyword arguments  [ kwargs ]
# only keyword arguments
def test(**data):
    print(data)


test(name='sandy', age=20,place='blr',city='blr',state='KA')

#  gives output in dictionary foramt









#
#
#
#
#
#
#
#
# res1 = 99

# def test(x,y,z):
#     # global res1,res2,res3
#     res1 = x + y + z
#     res2 = x - y - z
#     res3 = x * y * z
#     return res1,res2,res3

# op = test(20,10,5)
# print(list(op))
# #
# #
# print("res1 = " , res1)

def is_palindrome(s):
    """Checks if the given string s is a palindrome."""
    # Normalize the string by removing spaces and converting to lowercase
    s = s.replace(" ", "").lower()

    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True

    # Check the first and last characters
    if s[0] == s[-1]:
        # Recursive case: check the substring without the first and last characters
        return is_palindrome(s[1:-1])

    return False  # If characters do not match


# Example usage:
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("racecar"))  # Output: True



def factorial(n):
    """Returns the factorial of n using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage:
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(-3)) # Output: Factorial is not defined for negative numbers.









































