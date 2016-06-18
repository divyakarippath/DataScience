import pandas as pd
import statsmodels.api as sm
#Pandas is used to deal with tabular data
#read_excel returns a dataframe
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
#print first few lines
print df.count()
print df.head()

#Predict price based on mileage,model,and doors

df['Model_ord'] = pd.Categorical(df.Model).codes
print df.head()

x=df[['Mileage','Model_ord','Doors']]
y=df[['Price']]

x1 = sm.add_constant(x)
#print x1
est = sm.OLS(y,x).fit()
print est.summary()

#means of price for different number of doors
print y.groupby(df.Doors).mean()