import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
#fabricate a complex relationship between pagespeeds and purchase amount
pageSpeeds = np.random.normal(3.0,1.0,1000)
purchaseAmt = np.random.normal(50.0,10.0,1000)/pageSpeeds
plt.scatter(pageSpeeds,purchaseAmt)


#polynomeal regression , eg:4th degree
p4 = np.poly1d(np.polyfit(pageSpeeds,purchaseAmt,4))
xp = np.linspace(0,7,100)
plt.plot(xp,p4(xp),c='red')
plt.show()

#calculate r-square value
r2 = r2_score(purchaseAmt,p4(pageSpeeds))
print r2