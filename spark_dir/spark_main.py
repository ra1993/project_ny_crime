#so spark main can import spark tables
# from spark_tables import *
from spark_tables import *
#to get pg_etl.py to be able to use this module
# from .spark_tables import *
#so spark main can import spark tables

import findspark
findspark.init()
findspark.find()

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

MASTER_IP_ADDR= "192.168.0.179"

#Creating spark context object
sc = pyspark.SparkContext.getOrCreate()
#first component of a spark program is spark context
#spark context is the entrypoint for spark functionality and connects cluster with application
#if you want to create low level abstractions, you create objects with spark context
#so specify info of app you, like name, and master node's i.p address
#if you want to run spark in local mode you can put "local" in place of your i.p address
# configure = SparkConf().setAppName("process_crime_data").setMaster(MASTER_IP_ADDR)
# sc = SparkContext(conf=configure)

#Creating spark session object
spark = SparkSession \
        .builder \
        .appName("process_crime_data") \
        .config("config option", "config value") \
        .getOrCreate()

#getOrCreate() means if you already have a spark session running, instead of creating new one,
#old one will be returned and its parameters will be modified to new configs

spark.sparkContext.getConf().getAll()

def read_spark_data(file_path):
    return spark.read.csv(file_path, header=True)

def print_schema(df):
    return df.printSchema()

def get_df_size(df):
    return df.count()

def df_size_report(df_list):
    row_dict = {}
    
    for df in df_list:
        row_dict[df] = get_df_size(df)
    return row_dict

if __name__ == "__main__":
    print(df_size_report(df_list))