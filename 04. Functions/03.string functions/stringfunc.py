

# var = "python is easy"
# x = 30.7
 # print(type(var))


#  print(var)
#  print(var[2])
# print(var[-2])
# print(var[0:3])
#print(var[3:6])
#print(var[-4:])
#print(var[:3])
#print(var[::-1]) # reverse
#print(var[::2])  # jumping 

# + => concatenation

# x = 20
# y = 30
# res = x + y
# print(res)
#
#
# a = "santhosh"
# b = "bangalore"
#
# res = a + " " +  b
# print(res)



# #* - Duplication
#
# var = "India"
# res = var * 5
# print(res)

# for x in range(1,6):
#     print("$" * x)

############################# Functions ###############

# var = "pYThoN iS eSAy"
#
# res = var.capitalize() # only first letter will be capital
# print("capitalize format = " , res)
#
# res = var.title()
# print("title format = " , res)  # first letter of each word will be capital
#
# res = var.upper()
# print("upper format = " , res)  # all letters capital
#
# res = var.lower()
# print("lower format = " , res)  #all letter will be capital
#
# res = var.swapcase()
# print("swapcase format = " , res)  # upper becomes lower and lower becomes upper

# Ex : 1

# var = "there was a Network issue in servers"
# res = "NETWORK" in var.upper()  # gives boolean result
# print(res)

#
# var = "pYThoNiSeSAy"

# res = max(var)
# print("max value = " , res)   # A-Z counting (1-26)
# #
# res = min(var)
# print("minimum value = " , res)
#
#
# ### explaining ascii
#
# print(ord('z'))
# print(ord('A'))
#
# print(ord('⇴'))
#
# print(chr(67))


# for x in range(8600,8700):
#     print(chr(x))




# var = "pYThoN iS eSAy"
# res = len(var)
# print(res)


# Ex : 1 :
#
# while(True):

#     pwd = str(input("enter the pwd = "))

#     if(len(pwd) >= 8):
#         print("valid")
#         break
#     else:
#         print("invalid")




# Ex 2: userame pwd va;lidation prog

# user = "santhosh"
# pwd = "san@123"
# success = 0

# for x in range(3):
#     username = str(input("enter the user name = "))
#     password = str(input("enter the  password = "))

#     if(username == user and password == pwd):
#         print("welcome to home page ")
#         success = 1
#         break
#     else:
#         print("Wrong cred try again")

# if(success == 0):
#     print("account locked")






#
# var = "#######santhosh############kumar########"
# print(var)

# res = var.lstrip('#')
# print("left strip " , res)
#
# res = var.rstrip('#')
# print(" right strip " , res)
#
# res = var.strip('#')
# print(" full strip " , res) # it will remove left and right strips NOT in MIDDLE
#
# res = var.replace('#', ' ')
# print(res)
#
#
# pwd = 'santhosh123\n'
# res = pwd.strip('\n')
# print(res)
#
# ########################################
#
# var = """
# santhosh teaches python
# santhosh name is 2nd in the blogger list
# my parents kept my name as santhosh bcoz i will be happy
# """

# res = var.replace('santhosh', 'sandy')  
# # IN this number is given to  1 word to display as alias names 
# print(res)
#

# var = "india is 4th largest economy"

# res = var.startswith('india')
# print(res)

# Gives boolean TRUE OR FALSE

# res = var.endswith('Economy')
# print(res)



# pwd = "San@123 "  #space at end 
# res = pwd.endswith(' ')
# print(res)


# email = "sandy@gmail.com"
# res = email.endswith('@gmail.com')
# print(res)



#######################################
#split always stores in list
# var = "santhosh 560100 bangalore 9986019197"
# res = var.split(' ')
# print(res) #  stores in list 
# print(type(res))
#
#
# #
# email = "sandy@gmail.com"
# res = email.split('@')
# print(res) 

#
# data = ['a','b','c','d','e']
# res = '+'.join(data)
# print(res)

# dates = ['2024','3', '24']
# res = '/'.join(dates)
# print(res)


#
# var = "hi san hello san bye San"
# res = var.lower().count('san') # gives the first letter of index
# print(res)





# var = "today we have python class and python is easy"
# res = var.index('python')  # it will give index for first 
# print(res)



#
# log = """
# parse 1 Network
# favfvlkdfvvdfjkvhfvgdsjvh
# hjcashckljadckl;sdkvl;4
# aakcshaslkcjasl;
# dvmdc,vDF;
# dlfbkmdf'b;lg;ac;a
# ad;vkks'lvkmf'mvbg
# error: db conn failed
# innstances port is not active
# asjkhasck';lcv;ad
# cjas
# """

# errpos = log.index('error')
# print(errpos)
#
# errmsg = log[errpos:errpos+50]  # prints 50 characters from above log
# print(errmsg)
#


# # validation func


# var = "santhoshKUMAR"
# res = var.isalpha()
# print(res)

# var = "9986019197 "
# res = var.isdigit()
# print(res)

# var = 'san123'
# res = var.isalnum() # alpha-numeric
# print(res)


# var = "SANTHOSH LIKES WHEN THERE IS  A CONFIDENCE 9171819171919"
# # res = var.isupper()
# # print(res)

# res = var.islower()
# print(res)



#
# #
# var = "sandy@13141415^^&**(("
#
# import re
# var = "sandy@13141415^^&**(("
# spchar = re.findall('[0-9]', var)
# print(spchar)
#



# def search(char,str):
#     L=len(str)
#     print(L)
#     i = 0
#     while i < L:
#         if str[i]== char:
#             return 1
#             i = i + 1
#         return -1
#
# print(search("P","PYTHON"))

























