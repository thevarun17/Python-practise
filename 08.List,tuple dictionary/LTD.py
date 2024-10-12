# exlaioning the indexes
L1 = [10,20,30,40,50,60]

print(L1[0])
print(L1[-2])
print(L1[0:3])
print(L1[-2:])
print(L1[::2])
print(L1[::-1])


d1 = {'name':10,'age':20}
d2 = {'X':200}
print(d1.keys())
print(d2.values())
# res = d1 + d2
# res = d1.join(d2)


# # Concatenation
# L1 = [10,20,30]
# L2 = [40,50]
#
# res = L2 + L1
# print(res)
#

# t1 = ("san", "vijay", "ajit", "prem")
# t2 = ('roopa','kiran',10,'manjula',30.5)
#
# res = t1 + t2
# print(res)




# u get error if u concatenate dictionary
# D1 = {'A':20,'B':40}
# D2 = {'x':20,'y':40}
# res = D1 + D2
# print(res)


# Duplication
# L1 = [10,20,30]
# res = L1 * 3
# print(res)


# Index and index range
# L1 = [10,20,30,40,50]
# print(L1[0])
# print(L1[-1])
# print(L1[0:2])

# T1 = (10,20,30,40,50)
# print(T1[0])
# print(T1[-1])
# print(T1[0:2])


#  Membership operator

# var = "python is easy"
# res = "python" in var
# print(res)
#
#
# L1 = [10,20,30,40,50,1999,9,5432,54]
# res = 58 in L1
# print(res)

#

#tuple supports concatenation 
# t1 = ('a','b','c')
# t2 = ('x',10)

# res = t1 + t2
# print(res)



L1 = [10,20,30,40,50]
# res = len(L1)
res = max(L1)
print(res)


# D1 = {'A':10,'B':20,'C':30,'D':40,'E':2, 'F':1}

# print(max(D1))


##### Functions

L1 = [10,20,30,40,50]
T1 = (10,20,30,40,50)
D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}

# print(type(T1))
#
# res = len(L1)
# print(res)
#
# res = max(T1)
# print(res)
#
# res = min(D1)
# print(res)


# strlist = ['sandy','ajit', 'ravi', 'prem','santhosh']
# print(max(strlist))











# adding elements

# L1 =[10,20,30,40,50]
# L1.append(60)
# print(L1)


# T1 = (10,20,30,40,50)
# T1.append(60)
# print(T1)

#
# L1 =[10,20,30,40,50]
# L1.extend([60,70,80,90,100])
# print(L1)



# L1 = [10,20,30,40,50]
# # L1.insert(2,60)
# # print(L1)
#
# L1.insert(3,35)
# print(L1)





## adding elements in dictionary
#
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
# D1.setdefault('F',60)
# print(D1)
#
#adding all elements
# D1 = {'A':10,'B':20,'C':30,'D':40,'X':50}
# D2 = {'x':100,'Y':200 , 'Z':300}
# D1.update(D2)
# print(D1)






### delete elements


L1 = [10,20,30,40,50]
# del L1[-1]
# print(L1)
# del L1[0:2]
# del L1[-2:]
# del L1[-3:-1]
# del L1[::2]
# del L1[::-2]
# print(L1)

# Delete element in dictionary
#
# d1 = {'A':10 , 'B': 20 , 'C':30}
# del d1['A']
# print(d1)


# L1 = [10,20,30,40,50]
# # del L1[2]
#
# res = L1.pop(2) # or del L1[2]
# print(L1)
# print(res)


# L1.insert(2,res)
# print(L1)


##### Remove function

# L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]

names = ['san', 'tan' , 'jai', 'amit', 'raghu']
names.remove('amit')
print(names)


# L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]
# L1.remove(30)
# print(L1)


# L1.remove(20)
# print(L1)



L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]
# L1.remove(30)
# print(L1)
# L1.remove(30)
# print(L1)
# L1.remove(30)
# print(L1)

# L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]
# L1.clear()
# print(L1)




# L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)




# count function

# L1 = [30,30,10,20,30,40,50,30,60,30,70,30,80,30,90,30]
# L1.reverse()
#
# cnt = L1.count(30)
# print(cnt)
#
# while(cnt > 1):
#     L1.remove(30)
#     cnt -= 1
#
# print(L1)
#
# L1.reverse()
# print("final list = ", L1)


# L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]
#
# cnt = L1.count(20)
# print(cnt)
#
# if(cnt > 1):
#     print("duplicated lets remove the duplicates")
#
#     for x in range(cnt-1):
#         L1.remove(30)
# else:
#     print("Not duplicated")
#
# print(L1)
#



#
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
#
# del D1['B']
# print(D1)
#
# D1.clear()
# print(D1)
#
# L1 = [10,20,30,40,50]
# L1.clear()
# print(L1)


#
# # del L1
# # print(L1)


# t1 = (10,20,30,20,40,50,20)
# res = t1.count(20)
# print(res)


####### Update the value
#
#
# L1 = [10,20,30,40,50]
#
# L1[2] = 33
# print(L1)
#
# L1[0] = "abc"
# print(L1)
#
#
# L1[0:2] = ["ABCD", 1.5]
# print(L1)

# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
# D1['D'] = 60
# print(D1)




# T1 = (10,20,30,40,50,20,60,20)
# res = T1.count(20)
# print(res)

#
# L1 = [10,20,30,40,50,60,50,90,50,100,60,50]
# pos = L1.index(10,0,len(L1))
# print(pos)
#


#
# L1 = [4,2,1,3,5]
# # L1.sort(reverse=False)
# L1.sort()
# print(L1)
#
# L1.reverse()
# print(L1)


# t1 = (5,4,1,3,2)
# t1.sort()
# print(t1)


# L1 = []

# print("Before = ", L1)
#
# for x in range(5):
#     name = str(input("enter the name = "))
#     L1.append(name)
#
# print("After = " , L1)

# import sys
# print(sys.argv)
#

# names = ['raj','sandy','amit','krishna', 'Anu']
# names.sort()
# print(names)
#
# print(ord('A'))
# print(ord('a'))

####  Mistake in copy [ shallow and deep copy ]
#

# L1 = ['A','B','C','D','E']
# # Shallow copy [ shares same mem address ]
# # L2 = L1
# # Deep copy [ shares same mem address ]
# L2 = L1.copy()
#
# print(id(L1))
# print(id(L2))
#
# print("before delete")
# print(L1)
# print(L2)
#
# del L1[0:3]
#
# print("after delete")
# print(L1)
# print(L2)


# L1 = [10,20,30,40,50]
# L2 = L1.copy()
# print(L2)



# L1 = [10,20,30,40,50]
# print(type(L1))
# newvar = tuple(L1)
# print("converted list to tuple = " , newvar)
#

# T1 = (10,20,30,40,50)
# newlist = list(T1)
# print("converted tuple to list  = " , newlist)

#
# L1 = [1,2,3,1,2,5,6,2,3,6,2,4,1]
# S1 = list(set(L1))
# print(S1)


# L1 = [1,2,3,1,2,5,6,2,3,6,2,4,1]


D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}

mykeys = list(D1.keys())
myvalues = list(D1.values())
myitems = list(D1.items())

print(mykeys)
print(myvalues)
print(myitems)
#
# res = 10 in myvalues
# print(res)

# res = 200 in myvalues
# print(res)


L1 = [10,20,30,40,50]
for x in L1:
    if(x >= 25):
        print(x)



# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
#
# for k,v in D1.items():
#     if(v >= 25):
#         print(k , "====>" , v)



# allitems = {'horlicks':250,'juice':80 , 'oil':600 , 'chocolates':200, 'ironbox':700}
#
# for item,price in allitems.items():
#     if(price >= 500):
#         print(item, "====>" , price)







# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}

# # print("=====>", D1['X'])
#
# res = D1.get('X', 999)
# print(res)







#
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
#
# for k,v in D1.items():
#     if(v > 25):
#         print(k, "====>" , v)



# stud = {'rahul':90 , 'niki':87 , 'san':32, 'ganesh' : 91, 'shwetha': 31}
#
# for name, perc in stud.items():
#     if(perc < 35):
#         print(name, "===" , perc)







# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
# # print(D1['X'])
#
# res = D1.get('X', 999)
# print(res)

# data = {
#     'first' : 'santhosh',
#     'last' : 'yadav',
#     'age' : 22,
#     'place' : 'blr'
# }

# res = data['country']
# print(res)

# res = data.get('country', 'INDIA')
# print(res)










# L1 = [10,20,30,40,50]
# for x in L1:
#     print(x)



# data = [10,20,30,20,30,40,50,30,20,50,60,10,70]
# res = list(set(data))
# print(res)