import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

values = np.random.normal(10,0.5,10000)
plt.hist(values,50)
plt.show()

#first moment - mean
print np.mean(values)

#second moment - variance
print np.var(values)

#third moment - skew
print sp.skew(values)

#fourth moment kurtosis
print sp.kurtosis(values)