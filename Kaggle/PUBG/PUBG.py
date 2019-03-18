import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDRegressor, LassoCV, ElasticNet

data=pd.read_csv('train_V2.csv', nrows=100000)
test=pd.read_csv('test_V2.csv')
data.replace([np.inf, -np.inf], np.nan)
test.replace([np.inf, -np.inf], np.nan)
data.dropna()
test.dropna()

Id=test['Id']
target=data['winPlacePerc']

matchType=dict(zip(set(data['matchType']), range(len(set(data['matchType'])))))

data['matchType'] = [matchType[item] for item in data['matchType']]
test['matchType'] = [matchType[item] for item in test['matchType']]


data=data.drop(columns=['Id','groupId','matchId','winPlacePerc'])
# data=np.array(data)

test=test.drop(columns=['Id','groupId','matchId'])
# test=np.array(test)

clf=LassoCV()
clf.fit(data,target)
result=clf.predict(test)
# print(result)

output = pd.DataFrame( data={"id":Id, "winPlacePerc":result} )
print(output)
output.to_csv('ans.csv', index=False)

