# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

rim = {'M':1000,'CM':900, 'D':500, 'CD':400,  'C':100,  'XC':90,  'L':50,  'XL':40, 'X':10, 'IX':9,  'V':5, 'IV':4,  'I':1}
a=input()
ans=0
f=0
i=0
while (i<len(a)):
    if(rim.get(a[i:i+2])!=None):
        # print(a[i:i + 2])
        ans+=rim.get(a[i:i+2])
        i+=2
        f=1
    elif(rim.get(a[i])!=None):
        # print(a[i])
        ans+=rim.get(a[i])
        f=0
        i+=1
if(f==0):
    ans+=rim.get(a[len(a)-1])
print(ans)
