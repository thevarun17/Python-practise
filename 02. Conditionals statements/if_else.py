# simple if else block



# age = int(input("enter the age = "))
#
# if(age >= 26 and age <= 30):
#     print("eligible")
#     print("lets proceed")
# else:
#     print("not eligible")
#     print("lets stop here")


# continue

# Print odd numbers from 1 to 10
# for num in range(1, 11):
#     if num % 2 == 0:  # Check if the number is even
#         continue       # Skip the rest of the loop for even numbers
#     print(num)        # Print odd numbers



# Assert statement

# Giving warning  to your own code

# def divide(a, b):
#     assert b != 0, "The denominator cannot be zero!"  # Check that b is not zero
#     return a / b
#
# # Test the function
# result = divide(10, 0)  # This will work fine
# print("Result:", result)

# Uncommenting the following line will raise an AssertionError
# result = divide(10, 0)  # This will raise an error












# age = int(input("enter the age = "))
#
# if(age >= 21 and age <= 30):
#     print("eligible for marraige")
#     print("hello world")
# else:
#     print('Not eligible for marraige')
#     print("wait for some time")
















# # Nested if example

# age = int(input("enter the age = "))
#
# if(age >= 21):
#     if(age < 30):
#         print("correct age")
#     if(age >= 30 and age < 35):
#         print("Marry soon")
#     if(age >= 35):
#         print("No Marraige")
#     if(age == 25):
#         print("Sweet age")
# else:
#     print("Not eligible")



# # if -elif - else or switch cond

#
# age = int(input("enter the age = "))
#
# if(age >= 21):
#     if(age < 30):
#         print("correct age")
#     elif(age >= 30 and age < 35):
#         print("Marry soon")
#     elif(age >= 35):
#         print("No Marraige")
#     elif(age == 25):
#         print("sweet age")
# else:
#     print("not eligible")
#     print("else block")



# another example for switch
#
# c = str(input("enter the country name = "))
#
# if(c == "IND"):
#     print("Welcome to india")
#
# elif(c == "USA"):
#     print("Welcome to USA")
#
# elif(c == "UK"):
#     print("Welcome to UK")
#
# elif(c == "USA"):
#     print("Welcome to USA123457")
#
# else:
#     print("Country not supported")












######### LOOPS ############################
#

# nums = [10,20,30,40,50]
#
# for x in nums:
#     print(x+1,end= ' ')
#
# for x in nums:
    # a =print((x * 3),end=' ')
    # print((x * 3),end=' ')
    # a = x*3
    # print(a)
    # print(type(a))




# perc = [78,23,89,44,17,21,90,98]
# kl =[]
#
# cnt = 0
# for x in perc:
#     if(x > 60):
#         print(x)
#         kl.append(x)
#         cnt = cnt + 1
#
# print("total first class students cpunt = ", cnt)
# print(kl)

#
# names = ["kanna", "harish", "kiran", "preethi", "harsha", "satish"]
#
# for x in names:
#     print(x, end=" ")












# perc = [78,23,89,44,17,21,90,98]
#
# for x in perc:
#     if(x >= 80):
#         print(x)



# perc = [78,23,89,44,17,21,90,98,132,-30,113]
# #
# failc = 0
# firstc = 0
# secondc = 0
# thirdc = 0
# distc = 0
# invalidc = 0
#
# for x in perc:
#
#     if(x >= 0 and x < 35):
#         # print("====> Fail")
#         failc += 1
#     elif(x >= 35 and x < 50):
#         thirdc += 1
#     elif(x >= 50 and x < 60):
#         secondc += 1
#     elif(x >= 60 and x < 80):
#         firstc += 1
#     elif(x >= 80 and x <= 100):
#         distc += 1
#     else:
#         print("Invaid  = ", x)
#         invalidc += 1
#
#
# print("distinction  = " , distc)
# print("first  = ", firstc)
# print("second = " , secondc)
# print("third = ", thirdc)
# print("fail = " , failc)
# print("invalid = " , invalidc)



# shankar doubt answered

# x = int(input("enter the number = "))
#
# if(x >= 0 and x < 35):
#     print("failed")
# elif(x >= 35 and x < 50):
#     print("third")
# elif(x >= 50 and x < 60):
#     print("second")
# elif(x >= 60 and x < 80):
#     print("first")
# elif(x >= 80 and x <= 100):
#     print("distn")
# else:
#     print("failed")
#


###############################  LOOPS #######################################




# nums = [1,2,3,4,5,6,7,8,9,10]
#
# for x in nums:
#     print(x)

#
# for x in range(0,11):
#     print(x)




# for x in range(1,11):
#     print("sandy")


#
# x = 40
#
# if(x in range(50)):
#     print("hurray")
# else:
#     print("soo sad")
#


# for x in range(1,11):
#     if(x % 2 == 0):
#         print(x)









#
# import random
#
# otp = random.randrange(1000,9999)
# print(otp)



# inputotp = int(input("enter the otp = "))
#
# if(inputotp in range(1000,9999)):
#     print("otp is present")
# else:
#     print("otp is not present")






# conditional or while loop

#
# a = 5
#
# while(a > 0):
#     print(a)
#     a = a - 1


#
# for x in range(1,10):
#    print("A" * x)
#    print('*'* x)







# a = 50
#
# while(a > 0):
#     if(a%5 == 0):
#         print(a)
#         a = a - 1




#########################################################
#
#
# mynum = 3
# count = 0
# while(True):
#     guessnum = int(input("guess the number from 1 to 10 = "))
#     count = count + 1
#     if(mynum == guessnum):
#          print("bingo u guessed it right in counts ", count)
#          break
#     else:
#          print("sorry wrong guess pls try again ")
#




#### break , continue and pass
# break = loop termination statement
# continue = iteration skip statement
# pass = ignore statement


#
# nums = [10,20,30,40,50,60]
#
# for x in nums:
#     if(x == 30): # ignores the statement
#         pass
#     print(x)




# USERNAME PWD validation prog
#
# attempts = 3
#
# myuser = "sandy@gmail.com"
# mypass = "San@123"
# success = 0
#
# while(attempts > 0):
#     username = str(input("enter the user name = "))
#     password = str(input("enter the Password = "))
#
#     attempts = attempts - 1
#
#     if(username == myuser and password == mypass):
#         print("welcome to home page ")
#         success = 1
#         break
#
#     else:
#         print("sorry wrong cred try again attempts left ", attempts)
#
# if(success == 0):
#     print("You have exceeded your attempts and acc is locked")




####   Snake and ladder
#
# attempts = 0
# import random
# pos = 0
#
# while(pos <= 100):
#
#     dice = random.randrange(1,7)
#     attempts = attempts + 1
#     pos = pos + dice
#     print(pos)
#
#     if (pos == 100):
#         print("awesome i completed game in attempts = ", attempts)
#         break
#
#     if(pos > 100):
#         pos = pos - dice
#         print("your number cannot exceed 100 ", pos, dice , pos+dice)
#
#     if(pos == 23):
#         print("ladder from 23 to 67")
#         pos = 67
#
#     elif (pos == 45):
#         print("ladder from 45 to 88")
#         pos = 88
#
#     elif (pos == 17):
#         print("ladder from 17 to 77")
#         pos = 77
#
#     elif (pos == 62):
#         print("snake from 62 to 10")
#         pos = 10
#
#     elif (pos == 94):
#         print("snake from 94 to 12")
#         pos = 12
#
#     elif (pos == 32):
#         print("snake from 32 to 3")
#         pos = 3
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

















