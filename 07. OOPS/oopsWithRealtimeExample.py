
import os

class mod1:

    def __init__(self,cfiles,dfiles,F,M,L,d,m,y,var,email):
        self.cfiles = cfiles
        self.dfiles = dfiles
        self.F = F
        self.M = M
        self.L = L
        self.d = d
        self.m = m
        self.y = y
        self.var = var
        self.email = email


    def createfiles(self):
        ''' create files function will take n number of files and it will create it '''
        for x in self.cfiles:
            fvar = open(x, 'w')
            fvar.close()
            print("created the file ", x)


    def deletefiles(self):
        ''' delete files function will take n number of files and it will delete it '''
        for x in self.dfiles:
            os.remove(x)
            print("deleted file ", x)


    def formatname(self):
        fullname = self.F + ' ' + self.M + ' ' + self.L
        return fullname


    def formatdate(self):
        mydate = self.m + ":" + self.d + ":" + self.y
        return mydate


    def removespace(self):
        op = self.var.replace(' ', '')
        res = op.upper()
        return res


    def extractdata(self):
        temp = self.email.split('@')
        info = {}
        info['username'] = temp[0]
        info['domain'] = temp[1]
        return info


#cfiles,dfiles,F,M,L,d,m,y,var,email

obj1 = mod1(['a.txt','b.pdf','c.txt'],['a.txt','b.pdf'],'barsha','pd','saho','30','08','2002',"barsha likes travelling",'barsha@gmail.com')
obj2 = mod1(['x.txt'],['x.txt'],'vinay','kumar','gowda','15','05','1976',"vinay likes sleeping",'vinay@gmail.com')

# mod1.createfiles(obj1)

# mod1.deletefiles(obj1)
# mod1.deletefiles(obj2)

