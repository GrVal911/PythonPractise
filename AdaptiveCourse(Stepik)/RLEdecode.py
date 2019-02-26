a=input()
count=0
t=''
ans=''
for i in a:
    if (count==0):
        count+=1
        t=i
    elif (t==i):
        count+=1
    if(t!=i):
        if(count>1):
            ans+=str(count)+t
        else:
            ans+=t
        count=1
        t=i
if(count>1):
    ans+=str(count)+t
else:
    ans+=t
print(ans)