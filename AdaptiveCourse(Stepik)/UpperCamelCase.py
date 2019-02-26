a=input()
b=a[0].upper()
t=0
for i in range(1,len(a)):
    if (a[i]=='_'):
        t=1
    elif (t==0):
        b+=a[i]
    else:
        b+=a[i].upper()
        t=0
print(b)

