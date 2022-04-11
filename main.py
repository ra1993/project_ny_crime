import pandas as pd
import numpy as np

import sys
app_home = r"/home/richarda/Projects/udacity_projects/project_ny_crime/"
sys.path.append(app_home)

# from spark_dir.spark_main import *
from spark_dir.spark_tables import *
from pg_data_dir.pg_etl import *
from pg_data_dir.sql_queries import *
import configparser
# from aws.config import *

test_print = "This is test print for main"

if __name__ == "__main__":
    # print(crime_fact_insert)
    print(df_list)
    