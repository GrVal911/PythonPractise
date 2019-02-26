x,y=map(int, input().split())
mineMap=[]
for i in range (y):
    mineMap.append(list(input()))
# print(mineMap)

for i in range (len(mineMap)):
    for j in range (len(mineMap[i])):
        if(mineMap[i][j]=='.'):
            mineMap[i][j] = '0'

for i in range (len(mineMap)):
    for j in range (len(mineMap[i])):

        if (j!=(len(mineMap)-1)):
            if (mineMap[i][j+1]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (j!=0):
            if (mineMap[i][j-1]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (i!=(len(mineMap)-1)):
            if (mineMap[i+1][j]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (i!=0):
            if (mineMap[i-1][j]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (i!=(len(mineMap)-1) and j!=(len(mineMap)-1)):
            if (mineMap[i+1][j+1]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (i!=(len(mineMap)-1) and j!=0):
            if (mineMap[i+1][j-1]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (j!=(len(mineMap)-1) and i!=0):
            if (mineMap[i-1][j+1]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
        if (j!=0 and i!=0):
            if (mineMap[i-1][j-1]=='*'):
                if (mineMap[i][j]=='.'):
                    mineMap[i][j]='1'
                elif(mineMap[i][j].isdigit()):
                    mineMap[i][j]=str(int(mineMap[i][j])+1)
for i in range (y):
    print(''.join(mineMap[i]))


