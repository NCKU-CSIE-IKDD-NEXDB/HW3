import sys

from os.path import join
from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS
from numpy import array

def parseRating(line):
    fields = line.strip().split("::")
    return long(fields[3]) % 10, (int(fields[0]), int(fields[1]), float(fields[2]))

def parseMovie(line):
    fields = line.strip().split("::")
    return int(fields[0]), fields[1]

sc = SparkContext()

myRatingFile = open(sys.argv[2], 'r')
myRating = filter(lambda r: r[2] > 0, [parseRating(line)[1] for line in myRatingFile])
myRatingFile.close()
myRatingRDD = sc.parallelize(myRating, 1)

ratings = sc.textFile(join(sys.argv[1], "ratings.dat")).map(parseRating)

movies = dict(sc.textFile(join(sys.argv[1], "movies.dat")).map(parseMovie).collect())

numPartitions = 4
training = ratings.values().union(myRatingRDD).repartition(numPartitions).cache()
model = ALS.train(training, 8, 10, 0.1)

myRatingMovieId = set([x[1] for x in myRating])
candidates = sc.parallelize([m for m in movies if m not in myRatingMovieId])
predictions = model.predictAll(candidates.map(lambda x: (0, x))).collect()
recommendations = sorted(predictions, key=lambda x: x[2], reverse=True)[:50]

for index in xrange(len(recommendations)):
    print ("%d %s" % (index + 1, movies[recommendations[index][1]])).encode('ascii', 'ignore')
    if index == 9:
        break

sc.stop()
