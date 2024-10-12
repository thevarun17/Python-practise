
import os, shutil

# 1.access func check for file or folder existance

# res = os.access(r"C:\Users\DELL\Desktop\B-Python", os.F_OK)
# print(res)

# os.F_OK , os.R_OK , os.X_OK , os.W_OK

# res = os.access(r"C:\Users\DELL\Desktop\BESANT -python",os.R_OK)
# print(res)

# 2. delete the file
# os.remove(r'C:\Users\DELL\Desktop\BESANT -python\Os module\hi.txt')


#3. mkdir ( create folder )
# os.mkdir(r'C:\Users\DELL\Desktop\BESANT -python\RCB')


#4. delete an empty  folder
# os.rmdir(r'C:\Users\DELL\Desktop\BESANT -python\RCB')

# 5 deleting entire files and folder
# shutil.rmtree(r'C:\Users\DELL\Desktop\BESANT -python\RCB')

#6. creating recursive folderz

# os.makedirs(r'C:\Users\DELL\Desktop\BESANT -python\RCB\Bangalore\Kholi\ABD\Gayle\Dravid')
# shutil.rmtree(r'C:\Users\DELL\Desktop\BESANT -python\RCB')


# 7. rename
# old_file_name = 'C:\Users\DELL\Desktop\BESANT -python/varun.txt'
# new_file_name = 'C:\Users\DELL\Desktop\BESANT -python/APG.txt'
# os.rename(old_file_name,new_file_name)
# os.rename(r'C:\Users\DELL\Desktop\BESANT -python/goa.txt',r'mandya.txt')
# os.rename(r'C:\Users\DELL\Desktop\BESANT -python\Os module/mandya.txt',r'goa.txt')


# 8. : gets the current folder path

# res = os.getcwd()
# print(res)



# List the files in current path
# res = os.listdir()
# print(res)
#
# for x in res:
#     if(x.endswith('.py')):
#         print('TRUE')
#     else:
#         print("folder = ", x)


# 9.os.getcwd() -->> gets path of current directory

# print("before shifting my path = "  , os.getcwd())
# print(os.listdir())


# os.chdir () ---> used to change specified path
# os.chdir(r'D:\SANTHOSH\Batches\Batch106')

#os.getcwd() ----> after switching path gets all the directorys
# print("after shifting my path = "  , os.getcwd())
# print(os.listdir())



### sample prog to check the file exisatance

# res = os.access(r'D:\SANTHOSH\Work\capgemini\CG_Backup\abcd.txt', os.F_OK)
# print(res)
#
# if (res == True):
#     print("success email sent")
# else:
#     print("failure email sent")






# 11. only files

# shutil.copy(r'APG.txt' , r'./progs/APG.txt')




# 12. files & Folders

# moving file
# shutil.move(r'APG.txt' , r'./progs/APG.txt')



# moving folder
# shutil.move(r'rahul', r'./RCB')


#13. copying the folder

# shutil.copytree(r'ABD',r'./RCB/ABD')


#14 gets all environment variable data

# res = os.environ
#
# for x,y in res.items():
#    print(x  , "===>" , y)



# # 15. Environment variables

# res = os.getenv('YASHUSER')
# print(res)
# res = os.getenv('YASHPWD')
# print(res)


# # 16.
#
# res  = os.system('calc')
# print(res)




# res = os.system(r'type NUL > D:\SANTHOSH\Batches\Batch165-10am-Weekend-Python\kumudh.txt')
# print(res)






# res = os.system('pip3 install Asyncio')
# print(res)

#######################









 


















