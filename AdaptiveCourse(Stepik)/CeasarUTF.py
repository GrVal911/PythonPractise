n=int(input())
s=input().strip()
b=''
for i in s:
    print(ord(i))
    # b+=chr(ord(i)+n)
    if((ord(i)+n)%128591>=128511):
        b += chr(ord(i) + n)
    elif((ord(i)+n)%128591==0):
        b+=chr(128591)
    else:
        b+=chr(128511+(ord(i)+n)%128591)
print('Result: "'+b+'"')
# print(ord(🙏))
# print(ord(😀))