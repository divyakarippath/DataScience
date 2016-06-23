# Databricks notebook source exported at Thu, 23 Jun 2016 07:23:39 UTC
from pyspark import SparkConf,SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
rawData = sc.textFile("/FileStore/tables/dp736dao1466664806758/subset_small-50f68.tsv")
fields = rawData.map(lambda x:x.split("\t"))
documents = fields.map(lambda x:x[3].split(" "))

#Document names
documentNames = fields.map(lambda x:x[1])

#hash the word in document to their term frequencies
hashingtf = HashingTF(100000) #to save memory
tf = hashingtf.transform(documents) # each value ->term frequency of unique hash value

#calculating tf*idf score
idf = IDF(minDocFreq = 2).fit(tf)
tfidf = idf.transform(tf) # each value ->tf*idf of unique hash value of each document

#Test
gettysBurgTF = hashingtf.transform("Gettysburg")
gettysburgHashValue = int(gettysBurgTF.indices[0])

gettysburgRelevance = tfidf.map(lambda x: x[gettysburgHashValue])
zippedResults = gettysburgRelevance.zip(documentNames)

#print best result
print zippedResults.max()

