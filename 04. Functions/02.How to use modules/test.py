

import module1
import module2


module1.createfiles('a.txt','b.pdf')
module1.createfiles('x.txt','y.pdf', 'z.xlsx')
module1.createfiles(r'C:\Users\DELL\Desktop\B-Python\04. Functions\sandy1.txt', r'C:\Users\DELL\Desktop\B-Python\04. Functions\sandy2.txt' , r'C:\Users\DELL\Desktop\B-Python\04. Functions\sandy3.txt')



module1.deletefiles('a.txt','b.pdf')
module1.deletefiles(r'C:\Users\DELL\Desktop\B-Python\04. Functions\sandy1.txt', r'C:\Users\DELL\Desktop\B-Python\04. Functions\sandy2.txt' , r'C:\Users\DELL\Desktop\B-Python\04. Functions\sandy3.txt')

res = module1.formatname(M="kumar", F="Santhosh" , L = "Yadav")
print(res)


res = module1.extractdata('santhosh@gmail.com')
print(res)
print("success")

res = module2.mobval('8273787788')
print(res)


res = module2.totalbill(300,50,100,100)
print(res)


