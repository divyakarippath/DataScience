import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets
#fake income/age clusters for N people , K clusters
def createClusteredData(N,K):
    np.random.seed(10)
    pointsperCluster = float(N)/K
    X=[]
    y=[]
    for i in range(K):
        incomeCentroid = np.random.uniform(20000.0,200000.0)
        ageCentroid = np.random.uniform(20.0,70.0)
        for j in range(int(pointsperCluster)):
            X.append([np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,2.0)])
            y.append(i)
    X = np.array(X)
    y=np.array(y)
    return X,y
#visualize    
def plotPredictions(clf):
    xx, yy = np.meshgrid(np.arange(0, 250000, 10),
                     np.arange(10, 70, 0.5))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    plt.figure(figsize=(8, 6))
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
    plt.show()   
(X,y) = createClusteredData(100,5)
#visualize
plt.figure(figsize = (8,6))
plt.scatter(X[:,0],X[:,1],c=y.astype(np.float))
plt.show()

#partition graph into clusters using linear SVC
C=1.0
svc = svm.SVC(kernel='linear',C=C).fit(X,y)
plotPredictions(svc)

#predict
print svc.predict([50000,65])