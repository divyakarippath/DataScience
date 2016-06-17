import matplotlib.pyplot as plt
import numpy as np

#covariance between the pagespeeds and purchase amount of an ecommerce website

def scatter(X,Y):
    plt.scatter(X,Y)
    plt.show()
def def_mean(x):
    xmean = np.mean(x)
    return [xi-xmean for xi in x]
def covariance (X,Y):
    l=len(X)
    return np.dot(def_mean(X),def_mean(Y))/l-1
def correlation (X,Y):
    xstd = X.std()
    ystd = Y.std()
    return covariance(X,Y)/xstd/ystd    

pageSpeeds = np.random.normal(3,1,1000)
purchaseAmt = np.random.normal(50,10,1000)
scatter(pageSpeeds,purchaseAmt)
print covariance(pageSpeeds,purchaseAmt) #very close to zero

#Make purchaseamount a function of pageSpeed and see the increased covariance

purchaseAmtNew = np.random.normal(50,10,1000)/pageSpeeds
scatter(pageSpeeds,purchaseAmtNew)
print covariance(pageSpeeds,purchaseAmtNew) # far different from zero
print np.cov(pageSpeeds,purchaseAmtNew)
#correlation
print correlation(pageSpeeds,purchaseAmt)
print correlation(pageSpeeds,purchaseAmtNew)
print np.corrcoef(pageSpeeds,purchaseAmtNew)

#fabricate linear relationship
purchaseAmtNew1 = 100 - pageSpeeds*3
scatter(pageSpeeds,purchaseAmtNew1)
print correlation(pageSpeeds,purchaseAmtNew1)