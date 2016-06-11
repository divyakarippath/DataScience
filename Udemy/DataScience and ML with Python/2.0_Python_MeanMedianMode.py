import numpy as na
import matplotlib.pyplot as map
from scipy import stats

#income centered aroubd 27000,std deviation 150000, data points = 10000

income = na.random.normal(27000,15000,10000)
print na.mean(income)

# histogram showing income as 50 buckets
map.hist(income,50)
map.show()

#median
print na.median(income) # Mean and median are almost same

#Append a large valus to income
income = na.append(income,1000000000)

#print median and mean and see the difference
print na.mean(income)
print na.median(income)

#Mode

# Generate 500 random integeres between 15 and 90
ages = na.random.randint(15,high=90,size=500)
print ages
print stats.mode(ages)