from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
from pylab import *

#load iris dataset
iris = load_iris()
numSamples, numFeatures = iris.data.shape

#number of samples
print numSamples

#number of features/dimensions
print numFeatures

#species names
print list(iris.target_names)

#Transform the data to 2D using PCA
X = iris.data
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)
print pca.components_

#how much variance are preserved in each dimension
print pca.explained_variance_ratio_
print sum(pca.explained_variance_ratio_)

#plot the data


colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
        c=c, label=label)
pl.legend()
pl.show()