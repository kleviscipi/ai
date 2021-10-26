#./bin/pyspark

import pyspark;
sc = pyspark.SparkContext('local[*]')

textFile = sc.textFile("../README.md");

print(textFile.count())