import collections
a=[]
a=input().split()
c=collections.Counter(a)
print('%.2f' % float(c['A']/len(a)))