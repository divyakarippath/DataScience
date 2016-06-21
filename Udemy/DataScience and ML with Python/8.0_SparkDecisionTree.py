from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
sc = SparkContext(conf=conf)