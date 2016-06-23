from pyspark import SparkConf,SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from numpy import array
#conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
#sc = SparkContext(conf=conf)
#Load CSV file , filter out header lines with column names
def binary(x):
  if (x=='Y'):
    return 1
  else:
    return 0
def mapEducation(x):
  if (x == 'BS'):
    return 1
  elif(x == 'MS'):
    return 2
  elif(x=='PhD'):
    return 3
  else:
    return 0
def createLabelledPoints(fields):
  yearsExp = int(fields[0])
  employed = binary(fields[1])
  previousEmployers = binary(fields[2])
  educationLevel = mapEducation(fields[3])
  topTier = binary(fields[4])
  interned = binary(fields[5])
  hired = binary(fields[6])
  return LabeledPoint(hired, array([yearsExp,employed,previousEmployers,educationLevel,topTier,interned]))
  
rawData = sc.textFile("/FileStore/tables/h0n7898d1466645951833/PastHires.csv")
header = rawData.first()
rawData = rawData.filter(lambda x:x!=header)
#Split each line into a list based on comma delimiter
csvData = rawData.map(lambda x:x.split(","))
# Convert list to labeled point
trainingData = csvData.map(createLabelledPoints)



#Train decision tree classifier using our data set
model = DecisionTree.trainClassifier(trainingData, numClasses=2,
                                     categoricalFeaturesInfo={1:2, 3:4, 4:2, 5:2},
                                     impurity='gini', maxDepth=5, maxBins=32)

#Testing
testCandidate = [array([10,1,3,1,0,0])]
#convert this list into RDD
testData = sc.parallelize(testCandidate)
prediction = model.predict(testData)
results = prediction.collect()
for result in results:
  print result
#To print the decision tree
print model.toDebugString()




