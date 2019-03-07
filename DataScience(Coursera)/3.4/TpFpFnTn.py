import pandas
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score, precision_recall_curve

data = pandas.read_csv('classification.csv')
scores=pandas.read_csv('scores.csv')
# print(data['true'].values)
tn, fp, fn, tp = confusion_matrix(data['true'].values, data['pred'].values).ravel()
# print(tp, fp, fn, tn)

accuracy = accuracy_score(data['true'].values, data['pred'].values)
precision =precision_score(data['true'].values, data['pred'].values)
recall=recall_score(data['true'].values, data['pred'].values)
f1=f1_score(data['true'].values, data['pred'].values)
# print(accuracy,precision,recall,f1)

# print(roc_auc_score(scores['true'].values,scores['score_logreg'].values))
# print(roc_auc_score(scores['true'].values,scores['score_svm'].values))
# print(roc_auc_score(scores['true'].values,scores['score_knn'].values))
# print(roc_auc_score(scores['true'].values,scores['score_tree'].values))

names=['score_logreg', 'score_svm', 'score_knn', 'score_tree']
precMax=0
nameAns=''
for i in names:
    precision, recall, thresholds = precision_recall_curve(scores['true'].values,scores[i].values)
    for j in range(len(precision)):
        if recall[j]>=0.7 and precision[j]>precMax:
            precMax=precision[j]
            nameAns=i
print(precMax,nameAns)
