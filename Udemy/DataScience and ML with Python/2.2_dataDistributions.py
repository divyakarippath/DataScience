import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson
#Uniform distribution of 100000 data points between -10 and 10
values = np.random.uniform(-10,10,100000)
plt.hist(values,50)
plt.show()

#Normal distribution
x = np.arange(-3,3,.001)
plt.plot(x,norm.pdf(x))
plt.show()
mu= 5.0
sigma = 2.0
ndvalues = np.random.normal(mu,sigma,10000)
plt.hist(ndvalues,50)
plt.show()

#Exponential pdf
plt.plot(x,expon.pdf(x))
plt.show()

#Binomeal pmf
x1 = np.arange(0,10,.001)
plt.plot(x1,binom.pmf(x1,10,.5))
plt.show()

#Poisson pmf
mu=500
x2 = np.arange(400,600,.5)
plt.plot(x2,poisson.pmf(x2,mu))
plt.show()