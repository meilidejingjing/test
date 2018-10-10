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

'''
#5.2

class Account:
    def __init__(self,id_=0,balance=100,ann=0):
        self.__id = int(id_)
        self.__balance = float(balance)
        self.__ann = float(ann)
        print(self.__id)
    def getMon(self):
        self.Mon=self.__ann/12
        print(self.Mon)
    def winthdraw(self,a):
        self.w=self.__balance-a
    def desposit(self,b):
        self.d=self.w+b
        print(self.d)
    def getMonthly(self):
        self.Monthly=(self.__ann/12)*self.d
        print(self.Monthly)

A=Account(1122,20000,0.045)
A.getMon()
A.winthdraw(2500)
A.desposit(3000)
A.getMonthly()

'''
'''

#5.3
class fan:
    slow =1
    medium =2
    fast =3
    def __init__(self,speed=slow,radius=5,color='blue',on=False):
        self.__speed=speed
        self.__on=on
        self.__radius= float(radius)
        self.__color=color
        print('Speed:'+str(self.__speed))
        print('Radius:'+str(self.__radius))
        print('Color:'+str(self.__color))
        print('On:'+str(self.__on))

print('------1------')
fan(fan.fast,10,'yellow',True)
print('------2------')
fan(fan.medium)
'''
'''
#5.4 
import math

class RePoly:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=int(n)
        self.__side=float(side)
        self.__x=float(x)
        self.__y=float(y)
    def getPerimeter(self):
        self.p=self.__n*self.__side
        print("zhouchangwei  {}".format(self.p))
    def Area(self):
        self.s=pow(self.__side,2)
        self.t=math.tan(math.pi/self.__n)
        self.a=(self.__n*self.s)/(4*self.t)
        print("the mianji is  {}".format(self.a))
RePoly().getPerimeter()
RePoly().Area()
RePoly(6,4).getPerimeter()
RePoly(6,4).Area()
RePoly(10,4,5.6,7.8).getPerimeter()
RePoly(10,4,5.6,7.8).Area()

'''
'''
#5.5
class linear:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def issolvable(self):
        self.o = (self.a*self.d)-(self.b*self.c)
        if(self.o!=0):
            return True
        else:
            print("wujie")
    def getx(self):
        self.x = ((self.e*self.d)-(self.b*self.f))/self.o
        print("x={}".format(self.x))
    def gety(self):
        self.y=((self.a*self.f)-(self.e*self.c))/self.o
        print("y={}".format(self.y))
a,b,c,d,e,f=eval(input(">>"))
k =linear(a,b,c,d,e,f)
if(k.issolvable()==True):
    k.getx()
    k.gety()

'''

#5.6
class LinearaEquation:
x1,y1,x2,y2=eval(raw_input(">>yideduandian:"))
x3,y3,x4,y4=eval(raw_input(">>erdeduandian:"))
    





