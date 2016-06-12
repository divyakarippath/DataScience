import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100,50,10000)
plt.hist(incomes,50)
plt.show()

# standard deviation
print incomes.std()

#variance
print incomes.var()