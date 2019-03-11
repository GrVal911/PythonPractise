import pandas
import numpy as np
import math
from sklearn.metrics import roc_auc_score

def regression(x,y,k,w,c,eps,max_iter):
    w1,w2=w
    for i in range(max_iter):
        w1new=w1+k*np.mean(y*x[:,0]*(1-(1/(1+np.exp(-y*(w1*x[:,0]+w2*x[:,1]))))))-k*c*w1
        w2new=w2+k*np.mean(y*x[:,1]*(1-(1/(1+np.exp(-y*(w1*x[:,0]+w2*x[:,1]))))))-k*c*w2
        if np.sqrt(np.square(w1new-w1)+np.square(w2new-w2))<eps:
            break
        w1,w2=w1new,w2new
    predict=[]
    for i in range(len(x)):
        t1=-w1*x[i,0]-w2*x[i,1]
        # s=1/1+math.exp(-t1)
        predict.append(math.exp(-t1))
    return predict

data = pandas.read_csv('data-logistic.csv', header=None)
ans=data[0].values
target=data.iloc[:,[1,2]].values

p1=regression(target,ans,0.1,[0,0],0,0.00001,10000)
p2=regression(target,ans,0.1,[0,0],10,0.00001,10000)

print(roc_auc_score(ans,p1))
print(roc_auc_score(ans,p2))
