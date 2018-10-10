'''
url = 'http://www.baidu.com/?'
a = ('page=' )
b = '?wd=xiaopangzi'
for i in range(1,101):
    i+=1
    c =str(a)+i
    print(c)
    print '' .join((url,c,b))

'''

'''
#ep2:
A =[1,1,1,1,1,2,2,2,2,2,3]
A2 = []
for i in A:
    if i not in A2:
        A2.append(i)
print A2

'''


#ep3:
a4 = [['lyy',22,['360',100]],['jj',12,['baidu',10]],['tt',-1,['gle',0]]]
a4.sort(key = lambda x:x[2][1])
print a4









