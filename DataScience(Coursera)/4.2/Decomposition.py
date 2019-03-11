import pandas
import numpy as np
from sklearn.decomposition import PCA

data=pandas.read_csv('close_prices.csv')
djia=pandas.read_csv('djia_index.csv')
dataClf=data
del dataClf['date']
clf=PCA(n_components=10)
fit=clf.fit(dataClf)
X=pandas.DataFrame(fit.transform(dataClf))
Y=fit.transform(dataClf)
print(np.argmax(fit.components_[0]))
# print(dataClf.names())
c = np.corrcoef(X[0], djia['^DJI'])[0,1]
# print(c)


