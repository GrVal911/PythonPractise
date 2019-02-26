a=input().split()
b=input()
ans=[]
for i in range (len(a)):
    if (a[i]==b):
        ans.append(str(i))
if(len(ans)==0):
    print('None')
else:
    print(' '.join(ans))