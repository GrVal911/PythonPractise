a=[]
a=input().split()
dictVal={}
ans=[]
for i in a:

    if (dictVal.get(i.lower())!=None):
        dictVal.update({i.lower():dictVal.get(i.lower())+1})
    else:
        dictVal.update({i.lower(): 1})

for k,v in dictVal.items():
    print(k,v)
# print(' '.join(ans))


# a=[]
# a=input().split()
# b=set(a)
# for i in b:
#     a.remove(i)
# print(' '.join(set(a)))