a=input()
b=''
count=0

for i in range(len(a)):
    if (a[i].isdigit()):
        count+=1
    else:
        if(count!=0):
            b+=a[i]*int(a[i-count:i])
            count=0
        else:
            b += a[i]
print(b)