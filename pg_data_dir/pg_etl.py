import os
import sys
import psycopg2

#---get db connection
def create_db_conn():
    try:
        conn = psycopg2.connect("host=localhost dbname=pg_crime_db user=student password=1234")
        conn.autocommit = True
    except psycopg2.Error as e:
        print("ERROR: Could not create connection to Postgres DB")
    else:
        return conn

def create_cursor(conn_obj):
    try:
        cur = conn_obj.cursor()
        conn_obj.commit()
    except psycopg2.Error as e:
        print("Error: Couldn't create cursor object!")
        print(e)
    else:
        return cur
        
def create_table(conn, cur, sql_st):
    try:
        cur.execute(sql_st)
        print(f"""Table {sql_st} was successfully created!""")
        conn.commit()
    except psycopg2.Error as e:
        print("Error: Issue creating table!")
        print(e)

def drop_table(conn, cur, sql_st):
    try:
        cur.execute(sql_st)
        print(f"Table {sql_st} was successfully dropped!")
        conn.commit()
    except psycopg2.Error as e:
        print("Error: Issue creating table!")
        print(e)
    else:
        return "Table was dropped!"
        
def insert_data(conn, cur, df, sql_st):
    try:
        with open(df, 'r') as f_obj:
            cur.copy_from(f_obj, sql_st)
            conn.commit()
    except psycopg2.Error as e:
        print("Error: Couldn't load data into postgres")
        print(e)
    else:
        return "Data was loaded!"

if __name__ == "__main__":
    conn = create_db_conn()
    cur = create_cursor(conn)
    #Inserting schema
    # for table_st in create_table_queries:
    #      create_table(conn, cur, table_st)
    pass
