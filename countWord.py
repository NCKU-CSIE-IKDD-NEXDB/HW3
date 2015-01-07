from pyspark import SparkContext

sc = SparkContext()
file = sc.textFile("pg5000.txt")
counts = file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("result")
