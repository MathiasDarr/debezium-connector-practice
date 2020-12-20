# !/usr/bin/env python3
import psycopg2


def create_schema():
    query = 'CREATE SCHEMA IF NOT EXISTS snowpack;'
    params = ('schema_name', 'user_name')
    cur.execute(query, params)
    conn.commit()


def create_tables():
    create_trip_report_table = (""" CREATE TABLE IF NOT EXISTS reports(
                                report_id serial PRIMARY KEY ,
                                report_name VARCHAR NOT NULL);                                                    
                            """)

    create_table_queries = [create_trip_report_table]

    for query in create_table_queries:
        cur.execute(query)
    conn.commit()

def populate_table():
    insert_report = """INSERT INTO reports(report_name) VALUES (%s); """
    cur.execute(insert_report, ['trip1'])
    conn.commit()
if __name__ == '__main__':
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password="postgres",
                            database="snowpackDB",
                            options="-c search_path=snowpack")

    cur = conn.cursor()
    create_schema()
    create_tables()
    populate_table()