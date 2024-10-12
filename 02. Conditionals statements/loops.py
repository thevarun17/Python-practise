## Loops ###

# Example : 1
nums = [1,2,3,4,5,6,7,8,9,10]

for x in nums:
    print(x*10)
#
#
# # Example : 2
# perc = [34,56,78,90,21,67,98,31,76,54,67,42,16,78,19]

# failc = 0
# for x in perc:
#     if(x < 35):
#         print(x)
#         failc += 1
# #
# print("number of failed students = ", failc)










# for x in range(6):
#     print(x)
# #
#
# for x in range(1,11):
#     print(x, " ==> sandy")
#
#
# for x in range(1,11):
#     if(x % 2 != 0):
#         print(x)
#
# # print all nums which are divisible by 6 and 3 betweeen 1 to 100
#
for x in range(1,101):
    if(x%3 == 0 and x%6 == 0):
        print(x)


for letter in 'Python': # First Example
 if letter == 'h':      # h is skipped    contineue leavea nd 
  continue
 print ('Current Letter :', letter) 









# conditional or while loop

# Ex : 1

a = 5

while(a > 0):
    print(a)
    a = a - 1




for x in range(1,10):
    print("*" * x)
# Ecample 1 : for while loop

# a = 5
#
# while(a > 0):
#     print(a)
#     a = a - 1
#
# # print all nums divisible by 7 from 50 to 1 range
#
#
# a = 50
#
# while(a > 0):
#     if(a % 7 == 0):
#         print(a)
#     a = a - 1



###vbreak , continue , pass


nums = [10,20,30,40,50,60]

for x in nums:
    if(x == 40):
        pass # null
    print(x)



nums = [10,20,30,40,50,60]

for x in nums:
    if(x == 40):
        break   # out of loop
    print(x)




nums = [10,20,30,40,50,60]

for x in nums:
    if(x == 40):
      continue   # removes the condition and prints 
    print(x)


















