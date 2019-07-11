import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import Ridge

data = pandas.read_csv('salary-train.csv', dtype=str,nrows=10000).apply(lambda x: x.astype(str).str.lower())
# print(data.iloc[0,:])
for i in data:
    data[i]=data[i].replace('[^a-zA-Z0-9]', ' ', regex = True)
# print(data.iloc[0,:])

vectorizer = TfidfVectorizer(min_df=5)
X = vectorizer.fit_transform(data['FullDescription'])
# print(vectorizer.get_feature_names())

data['LocationNormalized'].fillna('nan', inplace=True)
data['ContractTime'].fillna('nan', inplace=True)

enc = DictVectorizer()
X_train_categ = enc.fit_transform(data[['LocationNormalized', 'ContractTime']].to_dict('records'))
# X_test_categ = enc.transform(data[['LocationNormalized', 'ContractTime']].to_dict('records'))
# print(X_train_categ)

params=hstack((X, X_train_categ))
# print(params)

clf = Ridge(alpha=1, random_state=241)
clf.fit(params,data['SalaryNormalized'])

dataTest = pandas.read_csv('salary-test-mini.csv', dtype=str).apply(lambda x: x.astype(str).str.lower())
# print(data.iloc[0,:])
for i in dataTest:
    dataTest[i]=dataTest[i].replace('[^a-zA-Z0-9]', ' ', regex = True)
# # # for i in range(1,len(dataTest)):

X_test = vectorizer.transform(dataTest['FullDescription'])
X_test_categ = enc.transform(dataTest[['LocationNormalized', 'ContractTime']].to_dict('records'))
X_test = hstack((X_test, X_test_categ))
# print(Xtest)
print(clf.predict(X_test))

