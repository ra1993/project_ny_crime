#Drop Tables

crime_fact_drop = ("""DROP TABLE IF EXISTS crime_fact""")
vic_dim_drop = ("""DROP TABLE IF EXISTS vic_dim""")
sus_dim_drop = ("""DROP TABLE IF EXISTS sus_dim""")
time_dim_drop = ("""DROP TABLE IF EXISTS time_dim""")
complaint_dim_drop = ("""DROP TABLE IF EXISTS complaint_dim""")
location_dim_drop  = ("""DROP TABLE IF EXISTS location_dim""")
jurisdiction_dim_drop = ("""DROP TABLE IF EXISTS jurisdiction_dim""")
housing_dim_drop = ("""DROP TABLE IF EXISTS housing_dim""")
arrest_info_drop = ("""DROP TABLE IF EXISTS arrest_info""")
pd_desc_drop = ("""DROP TABLE IF EXISTS pd_desc""")
law_charge_drop = ("""DROP TABLE IF EXISTS law_charge""")

#Insert statements

crime_fact_insert = ("""
    INSERT INTO crime_fact(
    complaint_num, 
    boro, 
    jurisdiction_code, 
    key_offense_class_code, 
    police_internal_classcode, 
    completion_status
    )VALUES(%s, %s, %s, %s, %s, %s)""")

vic_dim_insert = ("""
    INSERT INTO vic_dim(
    complaint_num, 
    vic_race, 
    vic_sex, 
    vic_age_group           
    )VALUES (%s, %s, %s, %s)""")

sus_dim_insert = ("""
    INSERT INTO sus_dim(
    complaint_num, 
    sus_race, 
    sus_sex, 
    sus_age_group
    )VALUES (%s, %s, %s, %s)""")

time_dim_insert = ("""" 
    INSERT INTO time_dim(
    complaint_num,
    report_date             
    )VALUES (%s, %s)""")

complaint_dim_insert = ("""
    INSERT INTO complaint_dim(
    complaint_num, 
    date_reported_known, 
    time_reported_known, 
    offense_description, 
    dt_reported_occur_unknown, 
    time_reported_occur_unknown    
    )VALUES (%s, %s, %s, %s, %s, %s)""")

location_dim_insert = ("""
    INSERT INTO location_dim(
    complaint_num, 
    boro, 
    park_name, 
    station_name, 
    patrol_boro, 
    in_or_around, 
    premesis_description, 
    transit_district, 
    x_coord_code, 
    y_coord_code, 
    lat, 
    lng, 
    lat_lon                                  
    )VALUES (%s, %s, %s, %s)""")

jurisdiction_dim_insert = ("""
    INSERT INTO jurisdiction_dim(
    jurisdiction_code, 
    complaint_num, 
    JURIS_DESC                                    
    )VALUES(%s, %s, %s)""")

housing_dim_insert = ("""
    INSERT INTO housing_dim(
    housing_code, 
    complaint_num, 
    name_of_occurance_loc                
    )VALUES(%s, %s, %s)""")

arrest_info_insert = ("""
    INSERT INTO arrest_info(
    arrest_code, 
    arrest_date, 
    arrest_boro, 
    arrest_precinct               
    )VALUES(%s, %s, %s, %s)""")

pd_desc_insert = ("""
    INSERT INTO pd_desc(
    police_internal_classcode, 
    class_code_description           
    )VALUES(%s, %s)""")

law_charge_insert = ("""
    INSERT INTO law_charge(
    law_code, 
    law_code_description             
    )VALUES(%s, %s)""")

drop_table_queries = [crime_fact_drop, vic_dim_drop, sus_dim_drop, 
                    time_dim_drop, complaint_dim_drop, location_dim_drop,
                    jurisdiction_dim_drop, housing_dim_drop, arrest_info_drop, 
                    pd_desc_drop, law_charge_drop]

insert_table_queries = [crime_fact_insert, vic_dim_insert, sus_dim_insert, time_dim_insert,
complaint_dim_insert, location_dim_insert, jurisdiction_dim_insert, housing_dim_insert, arrest_info_insert,
pd_desc_insert, law_charge_insert]
