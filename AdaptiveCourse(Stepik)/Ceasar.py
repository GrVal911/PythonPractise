ceasarList=' abcdefghijklmnopqrstuvwxyz'
n=int(input())
s=input().strip()
b=''
ceasarDictNum=dict(zip(range(27),ceasarList))
ceasarDictLet=dict(zip(ceasarList,range(27)))
for i in s:
    # print(ceasarDictNum.get((ceasarDictLet.get(i)+n)%27))
    b+=ceasarDictNum.get((ceasarDictLet.get(i)+n)%27)
print('Result: "'+b+'"')