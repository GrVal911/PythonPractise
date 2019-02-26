a=input()
b=input()
c=[]
count=0
t=0
while (t!=-1):
    t=a.find(b,count,len(a))
    c.append(str(t))
    count=t+1
if(len(c)>1):
    c.remove('-1')
print(' '.join(c))

# import re
# a=input()
# b=input()
# pattern=re.compile(b)
# result=pattern.findall(a)
# print(result)