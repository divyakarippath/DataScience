import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(0,0.5,10000)
plt.hist(values,50)
plt.show()
#50th percentile
print np.percentile(values,50)

print np.percentile(values,20)
print np.percentile(values,90)
#Median and percentile 50 same
print np.median(values)
