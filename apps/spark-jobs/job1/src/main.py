from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MLOps101-Job1") \
    .getOrCreate()

df = spark.read.csv("data.csv")
# Your processing logic here
