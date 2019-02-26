a=[]
a=input().split()
f=0
b=[]
for i in range(len(a)-1):
    if (abs(int(a[i])-int(a[i+1]))>1 or abs(int(a[i])-int(a[i+1]))<(len(a)-1)):
        b.append(abs(int(a[i])-int(a[i+1])))
    else:
        print('Not jolly')
        f=1
        break
if (f==0):
    b.sort()
    # print(b)
    for i in range(len(b)):
        if not(b[i]==i+1):
            print('Not jolly')
            f = 1
            break
if (f==0):
    print('Jolly')

