import numpy as np

#indentation based
listOfNumbers = [1,2,3,4,5,6]
for number in listOfNumbers:
    print number,
    if(number%2==0):
        print "even"
    else:
        print "odd"
print "all done"

# normal distribution of random parameters
A=np.random.normal(25.0,5.0,10)
print A

#Lists
x = [1,2,3,4,5,6,7]
print len(x) 
#sublist
# Elements till index 3
print x[:3]
# Elements after index 3
print x[3:]
#Last two elements
print x[-2:] 
#All the elements except last two
print x[:-2]

#Add a list to list
x.extend([8,9])
print x
#Add a new element (extend can also be used)
x.append(10)
print x
#index based
print x[6]
#sort function
x.sort() #Ascending
print x
x.sort(reverse=True) #Descending
print x