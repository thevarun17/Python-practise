
# # Reading the data from, text file
# fnames = open(r'C:\Users\DELL\Desktop\BESANT -python\User-Def-Module\x.txt')
#
# data = fnames.read()
# fnames.close()
#
# print(type(data))
# print(data)
#  ----------------------------------------------------
# #  readlines function
# fnames = open(r"C:\Users\DELL\Desktop\BESANT -python\User-Def-Module\x.txt")
# data1 = fnames.readlines()
# fnames.close()
#
# print(type(data1))
# print(data1)

# #-------------------------------------------------------------
# ## create a new text file and write data in text file

# fvar = open(r'C:\Users\DELL\Desktop\BESANT -python\User-Def-Module\good night.txt', 'w')
#
# data = """Congrats Modi for becoming
# PM 3 times in row
# June 8th is the
# swearing day
# Good luck
# # # """
# fvar.write(data)
#
# fvar.close()

# data = "Virat kholi we are watching you in WC"
#
#
#-------------------------------------------------------------------
# creating a new fuile ina folder and maintaing lines of text by steps
# fvar = open(r'path', 'a')
# data = ["kholi", 'Rohit', 'hardik', 'bumbra', 'pant']
# # data = "Virat kholi we are watching you in WC"
#
# newdata = []
# for x in data:
#     newdata.append(x+'\n')
#
#
# fvar.write(data)
# fvar.writelines(newdata)
#
# fvar.write(data)
# # fvar1.writelines(newdata)
# fvar.close()










####### append mode


# fvar = open(r'varun.txt' , 'w')
# fvar1 = open(r'varun.txt','a')
# # fvar1 = open(r'varun.txt','r')
# fvar1.write("good night modi")


# data = """Congrats Modi for becoming
# PM 3 times in row
# June 8th is the
# swearing day
# Good luck
# """
# data.append()
# fvar.write(data)
# data = fvar1.read()
#
# fvar1.write(data)
# fvar1.writelines(newdata)
# fvar1.close()
# print(data)

# fvar.close()














