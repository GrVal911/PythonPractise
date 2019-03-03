import numpy as np
import pandas
import sklearn
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

train = pandas.read_csv('perceptron-train.csv', header=None)
test = pandas.read_csv('perceptron-test.csv', header=None)
# print(train.iloc[:,[1,2]])
# print(train.iloc[:, 0])
clf = Perceptron(random_state=241)
clf.fit(train.iloc[:,1:], train.iloc[:, 0])
predictions = clf.predict(test.iloc[:,1:])
accur=accuracy_score(test.iloc[:, 0],predictions,normalize=True)
print(accur)

scaler = StandardScaler()
scaler.fit(train.iloc[:,1:])
dataTrain=scaler.transform(train.iloc[:,1:])
# scaler.fit(test.iloc[:,1:])
dataTest=scaler.transform(test.iloc[:,1:])

clf.fit(dataTrain, train.iloc[:, 0])
predictions = clf.predict(dataTest)
accurN=accuracy_score(test.iloc[:, 0],predictions,normalize=True)
print(accurN)
print(accurN-accur)
