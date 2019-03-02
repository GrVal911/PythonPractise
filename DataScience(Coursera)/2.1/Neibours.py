import numpy as np
import pandas
from sklearn.model_selection import KFold, cross_val_score
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

data = pandas.read_csv('wine.data', names=['Class'
    , 'Alcohol'
 	, 'Malic acid'
 	, 'Ash'
	, 'Alcalinity of ash '
 	, 'Magnesium'
	, 'Total phenols'
 	, 'Flavanoids'
 	, 'Nonflavanoid phenols'
 	, 'Proanthocyanins'
	, 'Color intensity'
 	, 'Hue'
 	, 'OD280/OD315 of diluted wines'
 	, 'Proline'])
# print(preprocessing.scale(data.head()))
# print(data.head())
data = np.array(pandas.read_csv('wine.data' ,header = None))


# data=preprocessing.scale(data)
kf=KFold(n_splits=5,shuffle=True, random_state=42)
k_max=0
mean_max=0
for i in range (1,51):
    knn_cv = KNeighborsClassifier(n_neighbors=i)
    cross=cross_val_score(knn_cv,preprocessing.scale(data[:,1:]),data[:,0],cv=kf,scoring='accuracy')
	# cross=preprocessing.scale(cross)
    print(cross)
    print(cross.mean(),i)
    print()
    if cross.mean()>mean_max:
        mean_max=cross.mean()
        k_max=i
print(k_max,mean_max)
