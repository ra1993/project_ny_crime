import findspark
findspark.init()
findspark.find()

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

def get_ip():
        with open('/home/ra-terminal/api_keys/google_key/i.p_address') as f_obj:
                i_p_addr = f_obj.readlines()[0]
        return i_p_addr

MASTER_IP_ADDR= get_ip()

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


if __name__ == "__main__":
    # print(df_size_report(df_list))
#     print(MASTER_IP_ADDR)
    pass