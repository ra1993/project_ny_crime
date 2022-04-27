from spark_dir.spark_util import read_spark_data
from g_drive import *
from google.colab import drive

drive.mount('/content/drive')

import sys
import os
#to allow the pg_etl module to use spark_tables

#Not using school demo, 
#NY_CRIME_PATH =  r'/home/richarda/datasets/ny_crime_datasets/ny_crime_data_main/NYPD_Complaint_Data_Historic.csv'
#NY_ARREST_PATH = r'/home/richarda/datasets/ny_crime_datasets/ny_arrest_data_main2/NYPD_Arrests_Data__Historic_.csv'
# NY_CRIME_PATH = ''
# NY_ARREST_PATH = ''


#importing from google drive
crime_file_data = search_file('NYPD_Complaint_Data_Historic.csv')
crime_file_id = crime_file_data.get('id')
arrest_file_id = search_file('NYPD_Arrests_Data__Historic_.csv')
arrest_file_id = arrest_file_id.get('id')

print(crime_file_id, "<-------------------->", arrest_file_id)
NY_CRIME_URL = f'https://drive.google.com/uc?export=download&id={crime_file_id}'
# NY_CRIME_URL = f'/content/drive/My Drive/Datasets/ny_crime_data/ny_crime_info_data/NYPD_Complaint_Data_Historic.csv' 
# NY_ARREST_URL = f'/content/drive/My Drive/Datasets/ny_crime_data/ny_arrest_data/NYPD_Arrests_Data_Historic_.csv'
NY_ARREST_URL = f'https://drive.google.com/uc?export=download&id={arrest_file_id}'

ny_crime_df = read_spark_data(NY_CRIME_URL)
ny_arrest_df = read_spark_data(NY_ARREST_URL)


# exploring new_york_crime_data and building tables
crime_fact = ny_crime_df[['CMPLNT_NUM','BORO_NM','JURISDICTION_CODE', 'KY_CD', 'PD_CD', 'CRM_ATPT_CPTD_CD']]
crime_fact = crime_fact.withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                        .withColumnRenamed("BORO_NM", "boro") \
                            .withColumnRenamed("JURISDICTION_CODE", "jurisdiction_code") \
                                .withColumnRenamed("KY_CD", "key_offense_class_code") \
                                    .withColumnRenamed("PD_CD", "police_dept_internal_code") \
                                        .withColumnRenamed("CRM_ATPT_CPTD_CD", "completion_status")

victim_dim = ny_crime_df[['CMPLNT_NUM', 'VIC_RACE', 'VIC_SEX', 'VIC_AGE_GROUP']]
victim_dim = victim_dim.withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                        .withColumnRenamed("VIC_RACE", "vic_race") \
                            .withColumnRenamed("VIC_SEX", "vic_sex") \
                            .withColumnRenamed("VIC_AGE_GROUP", "vic_age_group")
                                
sus_dim = ny_crime_df[['CMPLNT_NUM', 'SUSP_RACE', 'SUSP_SEX', 'SUSP_AGE_GROUP']]
sus_dim = sus_dim.withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                    .withColumnRenamed("SUSP_RACE", "sus_race") \
                        .withColumnRenamed("SUSP_SEX", "sus_sex") \
                            .withColumnRenamed("SUSP_AGE_GROUP", "sus_age_group")                   
                            
time_dim = ny_crime_df[['CMPLNT_NUM', 'RPT_DT']]
time_dim = time_dim.withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                    .withColumnRenamed("RPT_DT", "report_date")

complaint_dim = ny_crime_df[['CMPLNT_NUM', 'CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'OFNS_DESC', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM']]
complaint_dim = complaint_dim.withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                                .withColumnRenamed("CMPLNT_FR_DT", "date_reported_known") \
                                    .withColumnRenamed("CMPLNT_FR_TM", "time_reported_known") \
                                        .withColumnRenamed("OFNS_DESC", "offense_description") \
                                            .withColumnRenamed("CMPLNT_TO_DT", "dt_reported_occur_unknown") \
                                                .withColumnRenamed("CMPLNT_TO_TM", "time_reported_occur_unknown")

location_dim = ny_crime_df[['CMPLNT_NUM', 'BORO_NM', 'PARKS_NM','STATION_NAME','PATROL_BORO','LOC_OF_OCCUR_DESC','PREM_TYP_DESC','TRANSIT_DISTRICT','X_COORD_CD','Y_COORD_CD', 'Latitude', 'Longitude', 'Lat_Lon']]
location_dim = location_dim.withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                                .withColumnRenamed("BORO_NM", "boro") \
                                    .withColumnRenamed("PARKS_NM", "park_name") \
                                        .withColumnRenamed("STATION_NAME", "station_name") \
                                            .withColumnRenamed("PATROL_BORO", "patrol_boro") \
                                                .withColumnRenamed("LOC_OF_OCCUR_DESC", "in_or_around") \
                                                    .withColumnRenamed("PREM_TYP_DESC", "premesis_description") \
                                                        .withColumnRenamed("TRANSIT_DISTRICT", "transit_district") \
                                                            .withColumnRenamed("X_COORD_CD", "x_coord_code") \
                                                                .withColumnRenamed("Y_COORD_CD", "y_coord_code") \
                                                                    .withColumnRenamed("Latitude", "lat") \
                                                                        .withColumnRenamed("Longitude", "lng") \
                                                                            .withColumnRenamed("Lat_Lon", "lat_lon")

jurisdiction_dim = ny_crime_df[['JURISDICTION_CODE','CMPLNT_NUM','JURIS_DESC']]
jurisdiction_dim.withColumnRenamed("JURISDICTION_CODE", "jurisdiction_code") \
                    .withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                         .withColumnRenamed("JURIS_DESC", "juris_description")

housing_dim = ny_crime_df[['HOUSING_PSA','CMPLNT_NUM','HADEVELOPT']]
housing_dim = housing_dim.withColumnRenamed("HOUSING_PSA", "housing_code") \
                .withColumnRenamed("CMPLNT_NUM", "complaint_num") \
                .withColumnRenamed("HADEVELOPT", "name_of_occurance_loc")

#exploring arrest dataset
arrest_info = ny_arrest_df[['ARREST_KEY', 'ARREST_DATE', 'ARREST_BORO', 'ARREST_PRECINCT']]
arrest_info = arrest_info.withColumnRenamed("ARREST_KEY", "arrest_code") \
                .withColumnRenamed("ARREST_DATE", "arrest_date") \
                    .withColumnRenamed("ARREST_BORO", "arrest_boro") \
                        .withColumnRenamed("ARREST_PRECINCT", "arrest_precinct")

pd_desc = ny_arrest_df[['PD_CD', 'PD_DESC']]
pd_desc = pd_desc.withColumnRenamed("PD_CD", "internal_class_code") \
                .withColumnRenamed("PD_DESC", "class_code_description")

law_charge = ny_arrest_df[['LAW_CODE', 'LAW_CAT_CD']]
law_charge = law_charge.withColumnRenamed("LAW_CODE", "law_code") \
                    .withColumnRenamed("LAW_CAT_CD", "law_code_description")
                    
print("---------------")
print("---------------")

df_list= [crime_fact, victim_dim, sus_dim, time_dim, complaint_dim, location_dim, jurisdiction_dim, housing_dim, 
          arrest_info, pd_desc, law_charge]