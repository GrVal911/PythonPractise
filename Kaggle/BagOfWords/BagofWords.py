import pandas
import numpy as np
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

train=pandas.read_csv('labeledTrainData.tsv',header=0, delimiter="\t", quoting=3)
test = pandas.read_csv('testData.tsv', header=0, delimiter="\t", quoting=3 )
clean_train_reviews=[]
for i in range(0, len(train["review"])):
    clean_train_reviews.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train["review"][i], True)))
# print(clean_train_reviews)

vectorizer=CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000)
train_data_features = vectorizer.fit_transform(clean_train_reviews)
# print(vectorizer.get_feature_names())
np.asarray(train_data_features)

RFC=RandomForestClassifier(n_estimators=100)
RFC.fit(train_data_features,train['sentiment'])

clean_test_reviews = []
for i in range(0, len(test["review"])):
    clean_test_reviews.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(test["review"][i], True)))

test_data_features=vectorizer.transform(clean_test_reviews)
np.asarray(test_data_features)

result=RFC.predict(test_data_features)
output = pandas.DataFrame( data={"id":test["id"], "sentiment":result} )
print(output)
output.to_csv('Bag_of_Words_model.csv', index=False, quoting=3)

