from pyspark import SparkContext

sc = SparkContext()
file = sc.textFile("pg5000.txt")
count= file.map(lambda line: len(line.split())).reduce(lambda a, b: a + b)
print count
