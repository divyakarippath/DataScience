import numpy as np
from scipy import stats

A = np.random.normal(25.0, 5.0, 10000)
B = np.random.normal(26.0, 5.0, 10000)

print stats.ttest_ind(A, B)

B = np.random.normal(25.0, 5.0, 10000)

print stats.ttest_ind(A, B)

#sample size doesnt make much difference

A = np.random.normal(25.0, 5.0, 100000)
B = np.random.normal(25.0, 5.0, 100000)
print stats.ttest_ind(A, B)

A = np.random.normal(25.0, 5.0, 1000000)
B = np.random.normal(25.0, 5.0, 1000000)
print stats.ttest_ind(A, B)

print stats.ttest_ind(A, A) # Sanity test , t-statistic of 0 and p-value of 1