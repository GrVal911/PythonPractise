a,b=map(int,input().split('/'))
ans=[]
# print(a%b)
while (b!=0):
    ans.append(str(a//b))
    t=b
    b=a%b
    a=t
print(' '.join(ans))