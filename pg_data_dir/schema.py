import psycopg2
        
crime_fact_create = ("""CREATE TABLE IF NOT EXISTS crime_fact(
    complaint_num INT NOT NULL, 
    boro VARCHAR (50), 
    jurisdiction_code INT, 
    key_offense_class_code INT, 
    police_internal_classcode INT, 
    completion_status VARCHAR (20),
    PRIMARY KEY (complaint_num)
    )""")

vic_dim_create = ("""CREATE TABLE IF NOT EXISTS vic_dim(
    vic_id SERIAL NOT NULL,
    complaint_num INT NOT NULL, 
    vic_race VARCHAR (50), 
    vic_sex' VARCHAR (50), 
    vic_age_group INT,           
    PRIMARY KEY (vic_id)
    )""")
        
sus_dim_create = ("""CREATE TABLE IF NOT EXISTS sus_dim(
    sus_id SERIAL NOT NULL,
    complaint_num INT NOT NULL, 
    sus_race VARCHAR (50), 
    sus_sex VARCHAR (50), 
    sus_age_group VARCHAR (50),
    PRIMARY KEY (sus_id)              
    )""")

time_dim_create = ("""CREATE TABLE IF NOT EXISTS time_dim(
    time_id SERIAL NOT NULL,
    complaint_num INT NOT NULL,
    report_date date NOT NULL,
    PRIMARY KEY (time_id)
    )""")

complaint_dim_create = ("""CREATE TABLE IF NOT EXISTS complaint_dim(
    complaint_id SERIAL NOT NULL,
    complaint_num INT NOT NULL, 
    date_reported_known DATE, 
    time_reported_known DATE, 
    offense_description DATE, 
    dt_reported_occur_unknown DATE, 
    time_reported_occur_unknown DATE,                    
    PRIMARY KEY (complaint_id)
    )""")

location_dim_create = ("""CREATE TABLE IF NOT EXISTS location_dim(
    location_id SERIAL NOT NULL,
    complaint_num INT NOT NULL, 
    boro VARCHAR (20), 
    park_name VARCHAR (100), 
    station_name VARCHAR (50), 
    patrol_boro VARCHAR (50), 
    in_or_around VARCHAR (100), 
    premesis_description TEXT, 
    transit_district VARCHAR (50), 
    x_coord_code FLOAT, 
    y_coord_code FLOAT, 
    lat FLOAT, 
    lng FLOAT, 
    lat_lon FLOAT,                  
    PRIMARY KEY (location_id)                   
    )""")

jurisdiction_dim_create = ("""CREATE TABLE IF NOT EXISTS jurisdiction_dim(
    jurisdiction_code INT NOT NULL, 
    complaint_num INT, 
    JURIS_DESC VARCHAR (200),
    PRIMARY KEY (jurisdiction_code)                      
    )""") 

housing_dim_create = ("""CREATE TABLE IF NOT EXISTS housing_dim(
    housing_code INT NOT NULL, 
    complaint_num INT, 
    name_of_occurance_loc VARCHAR (100),           
    PRIMARY KEY (housing_code)           
    )""")

arrest_info_create = ("""CREATE TABLE IF NOT EXISTS arrest_info(
    arrest_code INT NOT NULL, 
    arrest_date DATE, 
    arrest_boro VARCHAR (50), 
    arrest_precinct VARCHAR (100),               
    PRIMARY KEY (arrest_code)
    )""")

pd_desc_create = ("""CREATE TABLE IF NOT EXISTS pd_desc(
    police_internal_classcode INT NOT NULL, 
    class_code_description VARCHAR (200),
    PRIMARY KEY (police_internal_classcode)
    )""")

law_charge_create = ("""CREATE TABLE IF NOT EXISTS law_charge(
    law_code INT NOT NULL, 
    law_code_description VARCHAR (200),
    PRIMARY KEY (law_code)
    )""")

create_table_queries = [crime_fact_create, vic_dim_create, sus_dim_create, time_dim_create, complaint_dim_create,
                    location_dim_create, jurisdiction_dim_create, housing_dim_create, arrest_info_create, pd_desc_create,
                   law_charge_create]