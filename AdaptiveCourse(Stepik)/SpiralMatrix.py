n=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
count=0
s=0
num=1
while(count<n):
    for i in range(n-count-1):
        # print(num)
        a[0+s][0+i+s]=str(num)
        num+=1
    for i in range(n-count-1):
        # print(num)
        a[0+i+s][n-s-1]=str(num)
        num+=1
    for i in range(n-count-1):
        # print(num)
        a[n-s-1][n-i-1-s]=str(num)
        num+=1
    for i in range(n-count-1):
        # print(num)
        a[n-i-1-s][0+s]=str(num)
        num+=1
    if(n-count-1==0):
        a[n-s-1][n-s-1]=str(num)
        # print(num)
    # print(' ')
    s+=1
    count+=2
for i in range(n):
    print(' '.join(a[i]))