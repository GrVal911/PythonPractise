n,m=map(int, input().split())
print(n,m)
a=[]
for i in range(n):
    a.append(input().split())
for j in range(m):
    t=[]
    for i in range(n):
        t.append(a[i][j])
    print(' '.join(t))
