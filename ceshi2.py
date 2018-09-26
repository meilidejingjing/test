
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
res = ''
for i in '2718775399@qq.com':
    res = res + chr(ord(i)+1)
print(res)
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


#2.3

#2.4

import random
a,b,c = eval(raw_input(">>shurusangeshu:"))
d = max(a,b,c)
e = min(a,b,c)
f = random.randrange(a,b,c)
if e<f<d:
    print(e,f,d)
else:
    print('FALSE')













