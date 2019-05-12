import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC, SVC
from sklearn.ensemble import GradientBoostingClassifier

data=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

# data=data.dropna()
# test=test.dropna()

ans=data['Survived']
Id=test['PassengerId']

data=data.drop(columns=['Embarked','Cabin','Name', 'Ticket','Survived','PassengerId'])
test=test.drop(columns=['Embarked','Cabin','Name', 'Ticket','PassengerId'])

data=data.fillna(data['Age'].median())
test=test.fillna(test['Age'].median())
# print(data.isna().sum())

gender=dict(zip(set(data['Sex']), range(len(set(data['Sex'])))))

data['Sex'] = [gender[item] for item in data['Sex']]
test['Sex'] = [gender[item] for item in test['Sex']]

X_train, X_test, y_train, y_test = train_test_split(data, ans, test_size=0.33, random_state=42)
# print(y_train)

# clf=SVC(kernel='linear',C=1)
# clf=KNeighborsClassifier(n_neighbors=50)
clf=GradientBoostingClassifier(n_estimators=1000)
clf.fit(X_train,y_train)
result=clf.predict(X_test)
print(accuracy_score(y_test,result))

# output = pd.DataFrame( data={'PassengerId':Id, 'Survived':result} )
# print(output)
# output.to_csv('ans.csv', index=False)