'''
#6.1
def jiance(a):
    n = 0
    for i in a:
        if i>='0' and i<='9':
            n+=1
    if len(a) == 11 and n ==9:
        if a[3]=='-' and a[6]=='-':
           a =  a.replace('-','0')
           if a.isalnum()==True:
               print('Valid SSN')
    else:
        print('Invalid SSN')

s = raw_input('play str ddd-dd-dddd:')
jiance(s)
'''
'''
#6.2
S = raw_input('>>shuruyichuanzifu:')
s = raw_input('>>shurulinyichuanzifu:')
if s in S:
    print("Yes")
else:
    print("No")
'''

'''
#6.3

def jiance(s):
    n = 0
    for i in s:
        if i>='0' and i<='9':
            n+=1
    if (len(s)>=8) and (s.isalnum()==True) and (n>=2):
        print('valid password')
    else:
        print('invalid password')

S = raw_input('>>')
jiance(S)

'''
'''
#6.4
def countLetters(s):
    n = 0
    for i in s:
        if i >='A' and i <= 'z':
            n+=1
    print('zimu:'+str(n))


S = raw_input('>>')
countLetters(S)

'''

'''

#6.5
def getNumber(uppercaseLetter):
    uppercaseLetter = uppercaseLetter.lower()
    if uppercaseLetter >='a' and uppercaseLetter <='c':
        return '2'
    elif uppercaseLetter >='d' and uppercaseLetter <='f':
        return '3'
    elif uppercaseLetter >='g' and uppercaseLetter <='i':
        return '4'
    elif uppercaseLetter >='j' and uppercaseLetter <='l':
        return '5'
    elif uppercaseLetter >='m' and uppercaseLetter <='o':
        return '6'
    elif uppercaseLetter >='p' and uppercaseLetter <='s':
        return '7'
    elif uppercaseLetter >='t' and uppercaseLetter <='v':
        return '8'
    elif uppercaseLetter >='w' and uppercaseLetter <='z':
        return '9'
    else:
        print uppercaseLetter
s = raw_input('Enter a string:')
S=''
for i in s:
    S = S+getNumber(i)
print(S)

'''
'''
#6.6
def reverse(s):
    print s[::-1]
S =raw_input('Enter str:')
reverse(S)

'''
'''
#6.7

def guize_1(n):
    if len(n)>=13 and len(n)<=16:
        if n.startswith('4')==True or n.startswith('5')==True or n.startswith('37')==True or n.startswith('6')==True:
            return True

def suanfa_1(n):
    sum_=0
    for i in n:
        z = int(i)*2
        if z>=10:
            a = z%10
            b = z/10
            z = a+b
        sum_=sum_+z
    return sum_

def suanfa_2(n):
    sum_=0
    for i in range(1,len(n)):
        if i%2!=0:
            sum_+=int(n[i])
    return sum_
def isValid(S):
    if guize_1(S)==True:
        if (suanfa_1(S)+suanfa_2(S))%10==0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

a = raw_input('Enter number:')
isValid(a)

'''

#6.8
def suanfa(s):
    sum_=0
    for i in range(0,len(s)):
        if i%2==0:
            sum_+=int(s[i])
        else:
            sum_+=3*int(s[i])
    d = 10-sun_%10
    if d == 10:
        d = 0
    return d
S = raw_input('Enter the first 12 digits of an ISBN-13 as a string:')
print('The ISBN-13 number is '+S+str(suanfa(S)))















