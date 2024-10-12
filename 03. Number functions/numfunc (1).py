# this is a number functions class

# syntax of function
# output  = functionname(input)

# 1. converts negative to positive value
# var = -10.5
# res = abs(var)
# print(res)
# #
# #
# 2. max : gives the max value
# res = max(20,6,90,100,50,-30)
# print(res)
#
# # 3. min : gives the min value
# res = min(20,6,90,100,50,-30)
# print(res)


# import math
# var = 10.2
# res = math.ceil(var)   # gives greater value (next value)
# print(res)
#
# res = math.floor(var)   #gives the same absolute value
# print(res)

# import math

# from IPython.core.profileapp import list_help

#
# var = 50
# res = math.sqrt(var)
# print(res)

# res = math.modf(var)  # it gives fractional part and integer part separately
# print(res)
#
# var = 45
# res = math.log(var)
# print(res)

# res = math.log10(var)
# res = math.tan(var)
# res = math.cosh(var)
# res = math.exp(var)
# res = math.degrees(var)

# dir will give list of all the functions present in the module or library
# print(dir(math))
#
# # dir will give information of all the functions present in the module or library
# print(help(math))
# list_help


# Random fuinctions
import random
#
# names = ['keerthi', 'aravind', 'prathik', 'apoorva', 'stenny', 'priya', 'anusha']
# random.shuffle(names)
# print(names)
# #
# #
# res = random.choice(names)
# print("my choice is = ", res)
#
#
# res = random.randrange(100000,999999) # selects number between
# print(res)
# print(help(random))


### some programs

# lottery = [120018001
# ,120018002
# ,120018003
# ,120018004
# ,120018005
# ,120018006
# ,120018007
# ,120018008
# ,120018009
# ,120018010
# ,120018011
# ,120018012
# ,120018013
# ,120018014
# ,120018015
# ,120018016
# ,120018017
# ,120018018
# ,120018019
# ,120018020
# ,120018021
# ,120018022
# ,120018023
# ,120018024
# ,120018025
# ,120018026
# ,120018027
# ,120018028
# ,120018029
# ,120018030
# ,120018031
# ,120018032
# ,120018033
# ,120018034
# ,120018035
# ]
# import random
#
# random.shuffle(lottery)
# random.shuffle(lottery)
# random.shuffle(lottery)
#
# print(lottery)
#
# print("are you ready for the winner announcement = ")
#
# inp = str(input("press ok for the first prize anouncement "))
# if(inp == "ok"):
#     firstprize = random.choice(lottery)
#     print("Congrats first prize goes to = ", firstprize)
#     lottery.remove(firstprize) #temproary removal
#
# inp = str(input("press ok for the second prize anouncement "))
# if(inp == "ok"):
#     secondprize = random.choice(lottery)
#     print("Congrats first prize goes to = ", secondprize)
#     lottery.remove(secondprize)
#
# inp = str(input("press ok for the third prize anouncement "))
# if(inp == "ok"):
#     thirdprize = random.choice(lottery)
#     print("Congrats first prize goes to = ", thirdprize)
#     lottery.remove(thirdprize)



## randrange()

# res = random.randrange(100000,999999)
# print(res)


##################################################################

# snake and ladder prog

# import random

# this pos variabvle holds the position of the pawn
# dice variable contains random number between 1 to 6
# dicecount will have the count of dices

# pos = 0
# dicecount = 0
#
# while(pos <= 100):
#     dice = random.randrange(1,7)
#     dicecount += 1
#
#     pos = pos + dice
#
#     print("current position is => " , pos)
#
#     if (pos == 100):
#         print("bibgo Gave over ", pos)
#         break
#
#
#     if(pos > 100):
#         pos = pos - dice
#
#     elif(pos == 4):
#         pos = 25
#         print("ladder came changing position to " , pos)
#
#     elif (pos == 13):
#         pos = 46
#         print("ladder came changing position to ", pos)
#
#     elif (pos == 27):
#         pos = 5
#         print("snake came changing position to ", pos)
#
#     elif (pos == 33):
#         pos = 49
#         print("ladder came changing position to ", pos)
#
#     elif (pos == 40):
#         pos = 3
#         print("snake came changing position to ", pos)
#
#     elif (pos == 42):
#         pos = 63
#         print("ladder came changing position to ", pos)
#
#     elif (pos == 43):
#         pos = 18
#         print("snake came changing position to ", pos)
#
#     elif (pos == 50):
#         pos = 69
#         print("ladder came changing position to ", pos)
#
#     elif (pos == 54):
#         pos = 31
#         print("sanke came changing position to ", pos)
#
#     elif (pos == 62):
#         pos = 81
#         print("ladder came changing position to ", pos)
#
#     elif (pos == 66):
#         pos = 45
#         print("snaker came changing position to ", pos)
#
#     elif (pos == 76):
#         pos = 58
#         print("snake came changing position to ", pos)
#
#     elif (pos == 89):
#         pos = 53
#         print("sanke came changing position to ", pos)
#
#     elif (pos == 99):
#         pos = 41
#         print("snake came changing position to ", pos)
#
#
# print("Game got completed in ", dicecount , " attempts")






















