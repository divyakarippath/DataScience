import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def predict(x):
    return slope*x + intercept
#Fabricate linear relationship between pagespeeds and purchaseamount
pageSpeeds = np.random.normal(3,1,1000)
purchaseAmt = 100-(pageSpeeds+np.random.normal(0,.1,1000)) * 3

plt.scatter(pageSpeeds,purchaseAmt)


#Linear Regression
slope,intercept,r_value,p_value,std_error = stats.linregress(pageSpeeds,purchaseAmt)
print r_value**2 # Which will be very close to 1 since we fabricated linear relationship

purchaseAmtPredicted = predict(pageSpeeds)
plt.plot(pageSpeeds,purchaseAmtPredicted,c='red')
plt.show()