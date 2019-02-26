import collections

a=input().split()
ans={}
for i in a:
    if(ans.get(len(i))==None):
        ans.update({len(i):1})
    else:
        ans.update({len(i):(ans.get(len(i))+1)})
ansD=collections.OrderedDict(sorted(ans.items()))
for k,v in ansD.items():
    print(str(k)+': '+str(v))