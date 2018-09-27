
'''
1.

import math
r = float(raw_input(">>"))
s = 2*r*(math.sin(math.pi/5))
area = 5*s*s/(4*math.tan(math.pi/5))
print('%.2f'%(area))

'''
'''
#2.
import math
x1,y1 = eval(raw_input(">>"))
x2,y2 = eval(raw_input(">>"))
r = 6371.01
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
d1 = (math.sin(x1))*(math.sin(x2))
d2 = (math.cos(y1-y2))
d3 = (math.cos(x1))*(math.cos(x2))*d2
d = r*(math.acos(d1+d3))
print(d)
'''
'''
#3.
import math
s = float(raw_input(">>shuru bianchang :"))
a1 = 5*s*s
a2 = 4*(math.tan(math.pi/5))
a = a1/a2
print('%.2f'%(a))
'''
'''
#4.
import math
n = int(raw_input(">>enter num:"))
s = float(raw_input(">>enter side:"))
a1 = n*s*s
a2 = 4*(math.tan(math.pi/5))
a = a1/a2
print('%.3f'%(a))
'''

'''
#5.

import math
a = int(raw_input(">>shu ru ACSII zhi :"))
A = chr(a)
print(A)
'''
'''

#6.

import math 
n = (raw_input(">>enter employee's name:"))
t = eval(raw_input(">>enter number of hours worked ina week:"))
p = eval(raw_input(">>enter pay rate:"))
ft = eval(raw_input(">>enter federal tax withholding rate:"))
st = eval(raw_input(">>enter state tax withholding rate:"))
print("employee name:{}".format(n))
print("hours in a week:{}".format(t))
print("hourly pay rate:${}".format(p))
print("gross pay:${}".format(t*p))
print("federal withholding(20.0%):${}".format(t*p*ft))
print("state withloding(9.0%):${}".format(t*p*st))
print("total deduction:${}".format(t*p*ft+t*p*st))
print("net pay:${}".format(t*p*(1-ft-st)))

'''
'''
#7.

import math
a = int(raw_input(">>enter a num:"))
b1 = a/1000
b2 = a/100%10
b3 = a/10%10
b4 = a%10
c = str(b4)+str(b3)+str(b2)+str(b1)
print(c)
'''
'''
#8.

text = 
new_text = ' '
for i in text:
    new = char(ord(i)+)
    new_text = new_text +new
    print(new_text)
    with open('text.txt','w') as f:
    f.write(new_text)

'''

'''
#2.1

import math
a,b,c = eval(raw_input(">>shuruzhi:"))
d = b*b-4*a*c
if d>0:
    r1 = ((-b)+(math.sqrt(d)))/2*a
    r2 = ((-b)-(math.sqrt(d)))/2*a
    print(r1,r2)

elif d == 0:
    r1 =((-b)+(math.sqrt(d)))/2*a
    print(r1)
else:
    print('the equation has no real roots')
'''
'''
#2.2

import random
a = random.randint(1,100)
b = random.randint(1,100)
c = a+b
sum = int(raw_input(">>shuruyigehe:"))
print(a)
print(b)
if sum == c:
    print('TRUE')
else:
    print('FALSE')
'''
'''
xingqiji

#2.3
from random import *
c = ['0','1','2','3','4','5','6']
a = int(raw_input(">>enter todays day:"))
b = int(raw_input(">>enter num of since day:"))
if (a+b)%7 ==0:
    print('future is 0')
if (a+b)%7 == 1:
    print('future is 1')
if (a+b)%7 ==2:
    print('future is 2')
if (a+b)%7 ==3:
    print('future is 3')
if (a+b)%7 ==4:
    print('future is 4')
if (a+b)%7 ==5:
    print('future is 5')
if (a+b)%7 ==6:
    print('future is 6')

'''

'''
#2.4

import math
a,b,c = eval(raw_input(">>shurusangeshu:"))
d = max(a,b,c)
e = min(a,b,c)
if e<a<d:
    print(e,a,d)
if e<b<d:
    print(e,b,d)
if e<c<d:
     print(e,c,d)
'''

'''
#2.5
import math
a,b = eval(raw_input(">>enter weight and price for package:"))
c,d = eval(raw_input(">>enter weight and price for package:"))
e = a/b
f = c/d
if e<f:
    print('package 1 has the better price')
else:
    print('package 2 has the better price')

'''
'''
panduannianyue
#2.6
import random
y = int(raw_input(">>shuruyuefen:"))
n = int(raw_input(">>shurunian:"))
if y == 2:
    if (n%400==0) | (n%4==0 & 100!=0):
        print(n,y,'runnian')
    else:
        print(n,y,'pingnian')
else:
    if (y==1) or (y==3) or (y==5) or (y==7) or (y==8) or (y==10) or (y==12):
        print(n,y,'31days')
    else:
        print(n,y,'30days')

'''


'''

#2.7

import  random
a = int(raw_input(">>shurucaicezhi:"))
b = random.randint(0,1)
print(b)
if a == b:
    print('True')
else:
    print('False')
'''
'''
#2.8
import random
a = int(raw_input(">>caicaiquan 0,1,2:"))
b = random.randint(0,2)
print(b)
if a>b:
    print('you won!')
elif a<b:
    print('you bad!')
else:
    print('pingjuo')
'''

'''
#2.10

from random import *
a = ['1','2','3','4','5','6','7','8','9','10','jack','queen','king']
b =['red','black','fang','mei']
c = choice(a)
d = choice(b)
print('the card you picked is the' ,c,'of',d)
'''

'''
#2.11
import math
a = int(raw_input(">>shuruyigesanweishu:"))
b = a/100
c = a%10
if b == c:
    print(a, 'is  palindrome')
else:
    print(a ,'is not  palindrome')

'''
'''
#2.12
import math
a,b,c = eval(raw_input(">>shurubianchang:"))
if (a+b)>c:
    print('fuhe')
else:
    print('bufuhe')
'''

'''

a = 'asdfg'
i = 0
while i<5:
    print(a[i])
    i += 1
'''

'''
import random
b = int(raw_input(">>shuruyigeshu:"))
a = random.randint(0,10)
while b!=a:
    if b>a:
        print('dale')
    else:
         print('xiaole')
         b = int(raw_input(">>shuruyigeahu:"))
print('zaishu')
'''
'''
sum_ =0
i = 0
while i<1001:
    sum_ +=i
    i +=1
'''
'''
sum_ = 0
for i in range(142):

    sum_+=i
    print(sum_)

'''

'''
jiujiuchengfabiao


#from_future_import print_function
for i in range(1,10):
    for j in range(1,i+1):
       print('{}x{}={}'.format(j,i,i*j),end='  ')
    print()
'''


'''
def suanchu1(a1,a2,a3):
    pass
    return a1,a2,a3

def suanchu2(a1,a2,a3):
    b = a1**2
    c = a2**2
    d = a3**2
    return b,c,d
def suanchu3(a1,a2,a3,b,c,d):
    e = b-a1
    f = c-a2
    g = d-a3
    print(e,f,g)
x,y,z = suanchu1(1,2,3)
m,n,w = suanchu2(x,y,z)
suanchu3(x,y,z,m,n,w)

'''















