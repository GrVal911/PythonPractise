import pandas
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor, RandomForestClassifier
from sklearn.metrics import log_loss
import math
import matplotlib.pyplot as plt



data=pandas.read_csv('gbm-data.csv')
target=np.array(data['Activity'])
del data['Activity']
data=np.array(data)
X_train, X_test, y_train, y_test =train_test_split(data, target,test_size=0.8,random_state=241, )

num=[1, 0.5, 0.3, 0.2, 0.1]
sc=[]
# sci=[]

# for i in num:
#     log=[]
#     GB=GradientBoostingClassifier(n_estimators=250, verbose=True, random_state=241,learning_rate=i)
#     test_deviance = []
#     train_deviance = []
#     GB.fit(X_train,y_train)
#     probs = GB.predict_proba(X_test)
#     # print(probs)
#     for j, pred in enumerate(GB.staged_decision_function(X_test)):
#         y_pred = 1.0 / (1.0 + np.exp(-pred))
#         test_deviance.append(log_loss(y_test,y_pred))
#     for j, pred in enumerate(GB.staged_decision_function(X_train)):
#         y_pred = 1.0 / (1.0 + np.exp(-pred))
#         train_deviance.append(log_loss(y_train,y_pred))
#     score = log_loss(y_test, probs)
test_deviance = []
GB = GradientBoostingClassifier(n_estimators=250, verbose=True, random_state=241, learning_rate=0.2)
GB.fit(X_train,y_train)
for j, pred in enumerate(GB.staged_decision_function(X_test)):
    y_pred = 1.0 / (1.0 + np.exp(-pred))
    test_deviance.append(log_loss(y_test, y_pred))

min=10
minI=-1
for i in range(len(test_deviance)):
    if test_deviance[i]<min:
        min=test_deviance[i]
        minI=i
print(min,minI)

RFC=RandomForestClassifier(random_state=241, n_estimators=minI)
RFC.fit(X_train,y_train)
probs = GB.predict_proba(X_test)
print(log_loss(y_test,probs))

    # sci.append(i)
    # print(score)
#     plt.plot(test_deviance, 'r', linewidth=2)
#     plt.plot(train_deviance, 'g', linewidth=2)
#     plt.legend(['test', 'train'])
# # plt.savefig('graph.jpg')
# plt.show()
# print(max(sc))
# print(sc)
    # print(test_deviance)
    # plt.plot(log, 'r', linewidth=2)



