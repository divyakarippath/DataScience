# Databricks notebook source exported at Thu, 23 Jun 2016 05:40:55 UTC
from pyspark.mllib.clustering import KMeans
from numpy import array,random
from math import sqrt
from pyspark import SparkConf,SparkContext
from sklearn.preprocessing import scale

K=5

def createClusteredData(N,K):
  random.seed(10)
  pointsPerCluster = float(N)/K
  X = []
  for i in range(K):
    incomecentroid = random.uniform(20000.0,200000.0)
    agecentroid = random.uniform(20.0,70.0)
    for j in range(int(pointsPerCluster)):
      X.append([random.normal(incomecentroid,10000.0),random.normal(agecentroid,2.0)])
  X = array(X)
  return X

def error(point):
  center = clusters.centers[clusters.predict(point)]
  return sqrt(sum([x**2 for x in (point-center)]))
#Load data and normalize it with scale
data = sc.parallelize(scale(createClusteredData(100,K)))
clusters = KMeans.train(data,K,maxIterations=10,runs=10,initializationMode="random")
resultRDD = data.map(lambda point:clusters.predict(point)).cache()
print "Counts by value"
counts = resultRDD.countByValue()
print counts
print "Actual assignments"
result = resultRDD.collect()
print result

#within set sum of squared errors
WSSE = data.map(lambda point:error(point)).reduce(lambda x,y:x+y)
print str(WSSE)

