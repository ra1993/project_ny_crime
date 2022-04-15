# from spark_dir.spark_tables import *
# from . import spark_tables

import findspark
findspark.init()
findspark.find()

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

MASTER_IP_ADDR= "192.168.0.179"

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

#Creating spark context object
sc = pyspark.SparkContext.getOrCreate()

#getOrCreate() means if you already have a spark session running, instead of creating new one,
#old one will be returned and its parameters will be modified to new configs

def read_spark_data(file_path):
    return spark.read.csv(file_path, header=True)

def print_schema(df):
    return df.printSchema()

def describe_df(df):
    #gives dataframe description. column name and column type
    return df.describe()

def get_df_size(df):
    return df.count()

def df_size_report(df_list):
    row_dict = {}
    #prints total rows for each df
    for df in df_list:
        row_dict[df] = get_df_size(df)
    return row_dict

def get_df_log(df, num):
    #can select how many rows should be shown
    return df.show(n=num)

def get_df_rows(df, num):
    
    return df.take(num)

def get_column_info(df, col):
    #get count, mean, stddev, min, max for column
    return df.describe(col).show()

def drop_duplicate(df, col):
    #drop duplicates and sort in for column data
    return df.select(col).dropDuplicates().sort()

def get_log_by_filter(df, target_col, target_val):
    #filtering df by column and value
    col_names = df.columns
    return df.select[(col_names)].where(df.target_col == target_val).collect()

def convert_to_pandas_df(df):
    #converting spark dataframe to pandas
    return df.toPandas()


if __name__ == "__main__":
    # print(df_size_report(df_list))
    pass