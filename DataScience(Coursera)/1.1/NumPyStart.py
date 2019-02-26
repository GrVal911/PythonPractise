import numpy as np
import pandas
from scipy.stats import pearsonr
from collections import Counter
# x=np.random.normal(1,10,(5,5))
# print(x)
#
# m=np.mean(x,0)
# std=np.std(x,0)
# xNorm=((x-m)/std)
# print(xNorm)
#
# m=np.mean(x)
# std=np.std(x)
# xNorm=((x-m)/std)
# print(xNorm)

# Z = np.array([[4, 5, 0],
#              [1, 9, 3],
#              [5, 1, 1],
#              [3, 3, 3],
#              [9, 9, 9],
#              [4, 7, 1]])
# r = np.sum(Z, 1)
# print (np.nonzero(r > 10)[0])
# ans=[]
# for i in range(len(r)):
#     if (r[i]>10):
#         ans.append(str(i))
# print(' '.join(ans))
#
# A = np.eye(3)
# B = np.eye(3)
# # print (A)
# # print (B)
# AB=np.vstack((A,B))
# print(AB)

f = open('ans.txt', 'w')
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

print(data['Sex'].value_counts()[0],data['Sex'].value_counts()[1])
print('%.2f' %float(data['Survived'].value_counts(normalize=True)[1]))
# a=float(data['Survived'].value_counts(normalize=True)[1])
# a*=100
# print(a)
# f.write('%.2f' %a)
print('%.2f' %data['Pclass'].value_counts(normalize=True)[1])
m=np.mean(data['Age'])
a=[]
for i in data['Age']:
    if i>0:
        a.append(i)
# print(a)
med=np.median(a)
print('%.2f' %m)
f.write('%.2f' %m)
# print(med)
print(pearsonr(data['SibSp'], data['Parch'])[0])
a=[]
fem=np.nonzero(data[:len(data)]['Sex']=='female')
for i in fem[0]:
    a.append(list(data[i:i+1]['Name']))
# print(a)
b=''
c=[]
for i in a:
    b=str(i[0])
    b=b.split('.')
    print(b[1])
    c.append(b[1])
# c.remove(c[0])
# print(c)
most_common,num_most_common = Counter(c).most_common(1)[0]
print(most_common,num_most_common)
# f.write(most_common)
# print(fem[0][1])

f.close()
# print(sorted(list(data['Age'])))