import pandas
from sklearn.svm import SVC

data = pandas.read_csv('svm-data.csv', header=None)
clf = SVC(C=100000, random_state=241, kernel='linear')
train=data.iloc[:,[1,2]]
ans=data.iloc[:,0]
clf.fit(train,ans)
print(clf.support_)
