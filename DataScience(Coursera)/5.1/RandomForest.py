import pandas
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import r2_score

data=pandas.read_csv('abalone.csv')
data['Sex'] = data['Sex'].map(lambda x: 1 if x == 'M' else (-1 if x == 'F' else 0))
# print(data['Sex'])
target=data['Rings']
del data['Rings']
kf = KFold(n_splits=5,random_state=1, shuffle=True)

max=0
maxI=-1

for i in range(1,51):
    sc=0
    clf=RandomForestRegressor(random_state=1,n_estimators=i)
    score = np.mean(
        cross_val_score(
            estimator=clf, X=data, y=target, cv=kf, scoring='r2'))
    if(score>0.52):
        print(i,score)

    # print(r2_score(target,predictions))
    # results = cross_val_score(clf, data, target, cv=kf)
    # print(results)


