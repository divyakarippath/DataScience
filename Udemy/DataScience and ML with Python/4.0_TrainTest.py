import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0,1.0,100)
purchaseAmt = np.random.normal(50.0,30.0,100)/pageSpeeds

#plt.scatter(pageSpeeds,purchaseAmt)
#plt.show()

trainX = pageSpeeds[:80]
trainY = purchaseAmt[:80]

testX = pageSpeeds[80:]
testY = purchaseAmt[80:]

#Train Set
x = np.array(trainX)
y=np.array(trainY)
p4 = np.poly1d(np.polyfit(x,y,8))

xp=np.linspace(0,7,100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
#plt.scatter(x,y)
#plt.plot(xp,p4(xp),c='red')
#plt.show()

#Test Set
testx = np.array(testX)
testy=np.array(testY)
plt.scatter(testx,testy)
plt.plot(xp,p4(xp),c='red')
plt.show()

#r2 score for test and train data sets
print r2_score(testy,p4(testx))

print r2_score(y,p4(x))

