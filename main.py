import pandas as pd
import numpy as np

import sys
from spark_dir.spark_main import *
from spark_dir.spark_tables import *
from spark_dir.spark_util import *

from pg_data_dir.pg_etl import *
from pg_data_dir.sql_queries import *
import configparser
# from aws.config import *



if __name__ == "__main__":
    #lists spark program's info
    spark_info = spark.sparkContext.getConf().getAll()
    print("=======",spark_info,"=======")
    
    conn = create_db_conn()
    cur = create_cursor(conn)
    
    # print(crime_fact.print_schema())
    # print(get_log_by_filter(crime_fact, "boro", "queens"))
    # print(crime_fact_insert)
    # print(df_list)
    # print(pg_etl_test)
    # print(insert_table_queries)
    # for idx, ins_tbl in enumerate(insert_table_queries):
    #     insert_data(conn, cur, df_list[idx], ins_tbl)
    spark.sql('''SELECT * 
              FROM crime_fact
              LIMIT 2''').show()
    # print(df_list)
    # print(df_size_report(df_list))
    # print(len(df_list), len(insert_table_queries))
    # pass
