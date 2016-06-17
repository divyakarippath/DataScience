from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3,3,.001)
#plt.plot(x,norm.pdf(x))
#plt.plot(x,norm.pdf(x,1,.5))
#plt.show()
plt.savefig("./Documents/Udemy_DataScience/plots/myPlot.png",format='png')

#adjust the axes
axes = plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1])
#Add grids
axes.grid()

#Change line types and colors
plt.plot(x,norm.pdf(x),'b-') # blue solid line
#plt.plot(x,norm.pdf(x,1,.5),'r:') #red vertical hashes
#plt.plot(x,norm.pdf(x,1,.5),'r--') #red vertical hashes
#plt.plot(x,norm.pdf(x,1,.5),'r-.') #hash and dot
#plt.show()

#Labelling axes and adding  legend
plt.xlabel("ages")
plt.ylabel("incomes")
#plt.plot(x,norm.pdf(x),'b-') 
#plt.plot(x,norm.pdf(x,1,.5),'r:')
#plt.legend(['a','b'],loc=4)
#plt.show()

#XKCD style
plt.xkcd()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30,10])
data = np.ones(100) # 100 points of 1
data[70:]-=np.arange(30)
plt.annotate('The day i realized\ni could cook',xy=(70,1),arrowprops=dict(arrowstyle='->'),xytext=(15,-10))
#plt.plot(data)
#plt.xlabel('time')
#plt.ylabel('overall health')
#plt.show()

#Pie charts
plt.rcdefaults()
vals= [12,55,4,32,14]
colors=['red','purple','green','yellow','blue']
labels=['India','China','USA','UK','Russia']
explode=[0,0,0,0,0.1]
#plt.pie(vals,colors=colors,labels=labels,explode=explode)
plt.title("Student Locations")

#Bar charts
plt.bar(range(0,5),vals,color=colors)
plt.show()

#Scatter plot
X=np.random.randn(500)
Y=np.random.randn(500)
plt.scatter(X,Y)
plt.show()

#Histogram
incomes = np.random.normal(27000,15000,10000)
plt.hist(incomes,50)
plt.show()

#Box and Whisker Plot
unifromskewed = np.random.rand(100)*100+40
positive_outliers = np.random.rand(100)*50+100
negative_outliers = np.random.rand(100)*-50*-100
data = np.concatenate((unifromskewed,positive_outliers,negative_outliers))
plt.boxplot(data)
plt.show()

