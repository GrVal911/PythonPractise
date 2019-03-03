import numpy as np
import pandas
from sklearn import datasets, preprocessing
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsRegressor

data=datasets.load_boston()
# print(data.data)
dataD=preprocessing.scale(data.data)
dataT=preprocessing.scale(data.target)
# print(dataD)
arr=np.linspace(1,10,200)
kf=KFold(n_splits=5,shuffle=True, random_state=42)
bestP=0
bestC=-1
for i in arr:
    KNR=KNeighborsRegressor(n_neighbors=5, weights='distance', metric='minkowski',p=i)
    cross=cross_val_score(KNR,dataD,dataT,cv=kf,scoring='neg_mean_squared_error')
    if max(cross)>bestC:
        bestC=max(cross)
        bestP=i
print(bestP,bestC)
