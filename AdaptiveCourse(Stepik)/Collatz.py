a=int(input())
b=[]
b.append(str(int(a)))
while True:
    if(a==1):
        break
    elif(a%2==0):
        a/=2
    else:
        a=a*3+1
    b.append(str(int(a)))
print(' '.join(b))