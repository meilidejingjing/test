'''
import requests
html = requests.get()
print(html)

'''
'''
#3.1
a = eval(raw_input(">>shurushu:"))
s1 =0
s2 =0
i = 0
j = 0
while a!=0:
    if a>0:
        s1=s1+a
        i+=1
    else:
        s2=s2+a
        j+=1
    a = eval(raw_input(">>shurushu:"))
x = s1/(i*1.0)
y = s2/(j*1.0)
print('{}:{}\n{}:{}'.format(i,x,j,y))

'''

'''
#3.2

n =1000
i =0
s =0
while i<13:
    n = n*(1+0.5)
    if i ==9:
        print('ten year late:'+str(n))
    if i>=9:
        s=s+n
    i+=1
print(s)
'''
'''
#3.4
k = 0
for i in range (100,1000):
    if (i%5==0) and (i%6==0):
        print('{}'.format(i),end= ' ')

        k+=1

    if k ==10:
        print()
        k=0
'''
'''
#3.5
n =0
m =0
while (n*n)<12000:
    n+=1
print(n)

while(m*m*m)<12000:
    m+=1
print(m-1)
'''
'''
#3.6
import math
x =eval(raw_input(">>loan amount:"))
y =eval(raw_input("number of years:"))
n =0.05
print('insrtest monthly payment tatal payment')
while n <0.08125:
    print(str(n*100)+ '%\t\t'+str((round(x*math.pow(1+n,y))/(12*y),2))+'\t\t'+str(round(x*math.pow(1+n,y),2)))
    n+=0.00125

'''
'''
#3.7

s1 =0
s2 =0
m =1
n =50000
while m<50001:
    s1 = s1+1/(m*1.0)
    m+=1
while n>0:
    s2 = s2+1/(n*1.0)
    n = n-1
print('s1='+str(s1))
print('s2='+str(s2))


'''

'''
#3.8


s = 0
n = 1
m = 3
while n<=97:
    s = s+n/(m*1.0)
    n+=2
    m+=2
print(s)
'''

'''
#3.9
s =0
k =1
f =0
i =1
while i<=100000:
    q = 1/(i*1.0)
    s =s+k*q
    k=k*-1
    i=i+2
    f=f+1
    if f ==5000:
        print('i='+str(i-1)+'\tp='+str(4*s))
        f=0

'''

#3.10

for i in range(1,10000):
    s =0
    for k in range(1,i):
        if i%k==0:
            s=s+k
    if i==s:
        print(i)

'''
#3.11
k = 0
a = [1,2,3,4,5,6,7]
for i in a:
    for j in a:
        k +=1
        print(i,j)

print('the total is ' ,k )

'''







