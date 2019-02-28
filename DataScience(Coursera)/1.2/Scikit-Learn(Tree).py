import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier
# X = np.array([[1, 2], [3, 4], [5, 6]])
# y = np.array([0, 1, 0])
# clf = DecisionTreeClassifier()
# clf.fit(X, y)
# print(type(clf))

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# print(data.columns)
for i in data.columns:
    if i!= 'Pclass' and i!='Fare' and i!='Age' and i!='Sex' and i!='Survived':
        del data[i]
# print(data.columns)
# print(surv)
# print(len(data))
# data=data.drop([1,2,3],0)
# print(len(data))
# print(data[:10])
# if np.any(data[5:6]['Age']):
# print(np.isnan(data[5:6]['Age']).any())
sex=[]
delet=[]
# print((data[1:2]['Sex']=='female').any())
for i in range(len(data)):
    if (data[i:i + 1]['Sex']=='male').any():
        sex.append(1)
    else:
        sex.append(0)
    if np.isnan(data[i:i+1]['Age']).any():
        delet.append(i+1)
        # data=data.drop(i+1,0)
        sex.pop(len(sex)-1)
data=data.drop(delet,0)
surv=data['Survived']
del data['Survived']
del data['Sex']
data['Sex']=sex
print(data.head())
# print(len(data),len(surv))
# print(data.head(10))
# print(data[:len(data)])
# print(np.all(np.isfinite(data)), np.any(np.isnan(data)))
clf = DecisionTreeClassifier(random_state=241)
clf.fit(data,surv)
importances = clf.feature_importances_
print(importances)