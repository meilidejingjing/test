'''
# 4.1

import math
def getPentagonalNumber(n):
    return n*(3*n-1)/2

k =0
for i in range(1,101):
    print('{}'.format(round(getPentagonalNumber(i))),end=' ')
    k+=1
    if k ==10:
        print( )
        k=0 

'''
'''
#4.2

def sumDigits(n):
    s=0
    while n!=0:
        s = s+n%10
        n = n/10
    return s
x = eval(raw_input('>>'))
print(sumDigits(x))

'''

'''
#4.3

import math
def displaySortedNumbers(num1,num2,num3):
    n =max(num1,num2,num3)
    m =min(num1,num2,num3)
    if num1!=n and num1!=m:
        return m,num1,n
    elif num2!=n and num2!=m:
        return m,num2,n
    else:
        return m,num3,n
x,y,z =eval(raw_input('enter three numbers:'))
print('the sorted numbers are{}'.format(displaySortedNumbers(x,y,z)))
'''

'''
#4.4

import math
def futureInverstmentValue(m,l,y):
    m = m*((1+l/12)**12)
    print(str(y)+'\t'+str(round(m,2)))
    return m
money = raw_input('the amount invested:')
li = raw_input('Annual interest rate:')

num_money = int(money)
num_li = int(li)
num_li = num_li*0.01

print('years\tFuture value')

for i in range(1,31):
    num_money = futureInverstmentValue(num_money,num_li,i)


'''
'''
#4.5
import math
def printChars(ch1,ch2,numberPerLine):
    for i in range(1,ord(ch2)-ord(ch1)):
        print('{}'.format(chr(ord(ch1)+i)),end='')
        if i%numberPerLine==0:
            print()
s1 = '1'
s2 = 'z'
n = 10
printChars(s1,s2,n)


'''

'''

#4.6
def numberofDaysInYear(year):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        print(str(year)+'  364')
    else:
        print(str(year)+'  365')
for y in range(2010,2021):
        numberofDaysInYear(y)


'''

'''
#4.7
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

x,y,n,m = eval(raw_input(">>"))
print(distance(x,y,n,m))


'''

'''
#4.8
print("p\t2^p-1:")
def s(a):
    c = 0
    for j in range(2,int(sqrt(a)+1)):
            if a%j == 0:
                c = 0
            else:
                c = 1
    return c
print("2\t3")
for i in range(1,32):
    c = pow(2,i)-1
    if(s(c)):
        print("%d\t%d"%(i,c))

'''
'''
#4.9

import time

now = time.time()
print(now)
mon = time.localtime(now)[1]
day = time.localtime(now)[2]
year = time.localtime(now)[0]
hour = time.localtime(now)[3]
mins = time.localtime(now)[4]
sec = time.localtime(now)[5]

print('Current date and time is '+ str(mon)+' '+str(day)+','+str(year)+' '+str(hour)+':'+str(mins)+':'+str(sec))
'''

#4.10

import random
def saizi():
    x = random.randint(1,6)
    y = random.randint(1,6)
    s = x+y
    print('you rolled'+str(x)+'+'+str(y)+'='+str(s))
    return s
S =saizi()
if (S==2) or (S==3) or (S==12):
    print('you lose')
elif (S==7) or (S==11):
    print('YOU WIN')
else:
    n = S
    S = saizi()
    while (S!=7) and (S!=n):
        S = saizi()
    if S ==7:
        print('you lose')
    else:
        print('you win')
















