# import re

# var = "my mobile nums are 7411694426 and 8116165656 and 9986019197abcd"
# temp = var.split(' ')
# print(temp)
# #
# for x in temp:
#     if(len(x) == 10 and x.isdigit()):
#         print(int(x))




# import re

# var = "today python is easy to learn i love python and python rocks"

# res = re.match('today', var)
# print(res)

# res = re.search('python', var)
# print(res)
# #
# res = re.findall('python', var)
# print(len(res))
# print(res)



# import re
# var = "today python is easy to learn i love python and PYthon rocks PYThoN"

# res = re.findall('python',var,re.I)
# print(res)
#
# res = re.sub('python' , 'java' ,var.lower())
# print(res)




# regex examples

# import re
# var = "my mobile nums are 717171 and 7411694426 and 9986019197abcd and 9986019193 and 9816167888xyz"
# pat  = '[0-9]{6,10}'
# res = re.findall(pat,var)
# print(res)



#




# import re
# var = "my fav dest places are SINGAPORE and MALDIVES and LOSVEGAS and BALI and GOA"
#
# pat = '[A-Z]{3,}'
# countries = re.findall(pat,var)
# print(countries)



# import re
# var = """
# KEERTHANA id is ABC1234
# ANU id is XYZ9875
# MAINAK id is PQE4545
# """
#
# patn = '[A-Z]{3,}'
# patid = '[A-Z]{3}[0-9]{4}'
#
# names = re.findall(patn,var)
# ids = re.findall(patid,var)
#
# print(names)
# print(ids)







# import re
# var = """
# Mahesh likes CHICKEN
# Prakash likes BIRYANI
# Resmi likes JAMOON
# """
#
# patn = '[A-Z][a-z]{1,}'
# patf = '[A-Z]{3,}'
# patl = '[a-z]{1,}'
#
# names = re.findall(patn, var)
# food = re.findall(patf, var)
#
#
# print(names)
# print(food)

#
#



















# import re
# var = """
# India ip address is 192.3.4.67
# Australia ip address is 23.123.5.4
# Canada ip address is 165.211.90.43 and 1.45.78.65
# """
#
#
# patc = '[A-Z][a-z]{1,}'
# patip = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
#
#
# countries = re.findall(patc, var)
# ips = re.findall(patip,var)
#
# print(countries)
# print(ips)








#
# import re
# var = """
# 16.09.2000 and email is chethanasonami16092000@gmail.com
# 26/11/1994 and email is dipalioj26@reddiff123.com
# 26-04-2000 and email is JayaShreebharathi10@yahoo.com
# """
#
# patd = '[0-9]{1,2}[^A-Za-z0-9][0-9]{1,2}[^A-Za-z0-9][0-9]{4}'
# pate = '[a-zA-Z0-9]{1,}[@][a-zA-Z0-9]{1,}[.]com'
#
#
#
# dates = re.findall(patd,var)
# emails = re.findall(pate, var)
#
# print(dates)
# print(emails)



# file example to format uneven spaces
# import re
#
# fvar = open(r'D:\SANTHOSH\Batches\Batch138-8am\files\data.txt', 'r')
# info = fvar.read()
# fvar.close()
#
# print(info)
#
# res = re.sub('[ ]{1,}', ' ', info)
#
# fvar = open(r'D:\SANTHOSH\Batches\Batch138-8am\files\data.txt', 'w')
# fvar.write(res)
# fvar.close()




# # password Validation function
# import re
# pwd = str(input("enter the password = "))
#
# ## for students reference
# caps = re.findall('[A-Z]' , pwd)
# print(caps)
# lows = re.findall('[a-z]', pwd)
# print(lows)
#
# caps = len(re.findall('[A-Z]', pwd))
# lows = len(re.findall('[a-z]', pwd))
# digs = len(re.findall('[0-9]', pwd))
# spec = len(re.findall('[^A-Za-z0-9]', pwd))
# pwdlen = len(pwd)
#
# if(caps > 0 and lows > 0 and digs > 0 and spec > 0 and pwdlen >= 8):
#     print("Valid Password")
# else:
#     print("Invalid password")
#
#
# #
# #
# print(caps)
# print(lows)
# print(digs)
# print(spec)
# print(pwdlen)
#
#
# #
# import re
# var = """
# hello  $$$$ %%%% * ( )))           all            how
# are you        $$$$ %%%% * ( )))         hope
# all are   $$$$ %%%% * ( )))      revising            python
# """
#
# res = re.sub('[ ]{1,}', ' ', var)
# print(res)
#
# patsp = '[ ]'
#
# # patsp = '[ ]{1,}'
# patc = '[^A-Za-z0-9]' + '|' +  patsp
# op = re.sub(patc, ' ', res)
# print(op)


################grouping###########################
