'''
#_*_coding:utf8-
'''
'''
class haha:
    def __init__(self):
        self.shuai = 'lalala'
        self.chou = 'hahaha'
    def fuc(self):
        print self.shuai
        print self.chou
if __name__=='__main__':
    haha().fuc()

'''
'''
class jiou:
    def __init__(self):
        self.num =39
    def check(self):
        if self.num%2 == 0:
            print '[+] ou'
        else:
            print '[+] ji'
if __name__ =='__main__':
    jiou().check()


'''

'''
class my:
    def __init__(self):
        self.caichan = 1000
    def showmy(self):
        print '[+] my',self.caichan
class hw(my):
    def __init__(self):
        my.__init__(self)
        self.hw = 10
    def showhw(self):
        print '[+] hwcaichan',self.caichan
hw().showmy()
'''

'''
#5.1
class rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        res = self.width * self.height
        print res
    def getP(self):
        res2 = 2*(self.width+self.height)
        print res2
rectangle(4,40).getArea()
rectangle(4,40).getP()
'''
#5.2

class Account:
    def __inti__(self):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = 0
    def __getMonthlyInterestRate__(self):


    def __getMonthlyInterest(self):









