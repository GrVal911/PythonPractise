import operator
a=[]
a=input().split()
opers = {'plus': operator.add(int(a[0]),int(a[2])), 'minus': operator.sub(int(a[0]),int(a[2])),
         'multiply': operator.mul(int(a[0]),int(a[2])), 'divide': operator.floordiv(int(a[0]),int(a[2])) }
print(opers.get(a[1]))