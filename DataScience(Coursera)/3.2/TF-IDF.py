from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, KFold
import numpy as np

newsgroups = datasets.fetch_20newsgroups(
                    subset='all',
                    categories=['alt.atheism', 'sci.space']
             )
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups.data)
# Y = vectorizer.transform(newsgroups.data)
feature_mapping = vectorizer.get_feature_names()

cv = KFold(n_splits=5, shuffle=True, random_state=241)
grid = {'C': np.power(10.0, np.arange(-5, 6))}
clf = SVC(random_state=241, kernel='linear')
gs = GridSearchCV(clf, grid, scoring='accuracy', cv=cv)
gs.fit(X,newsgroups.target)
best_C = gs.get_params()["estimator__C"]
gs = SVC(C=best_C, kernel='linear', random_state=241)
print(gs)




