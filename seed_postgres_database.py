# !/usr/bin/env python3
import psycopg2


def create_schema():
    query = 'CREATE SCHEMA IF NOT EXISTS snowpack;'
    params = ('schema_name', 'user_name')
    cur.execute(query, params)
    conn.commit()


def create_tables():
    create_trip_report_table = (""" CREATE TABLE IF NOT EXISTS trip_reports(
                                trip_id serial PRIMARY KEY ,
                                trip_name VARCHAR NOT NULL,
                                trip_report VARCHAR NOT NULL,
                                elevationGain float NOT NULL,
                                mileage INT NOT NUll,
                                trip_date DATE NOT NULL,
                                locations text[] NOT NULL);                                                    
                            """)

    trip_location =(""" CREATE TABLE IF NOT EXISTS geographic_location(
                                elevation INT NOT NULL,
                                lat INT NOT NULL,
                                lng INT NOT NULL,
                                location_name VARCHAR NOT NULL,
                                terrain_features text[], 
                                water_availability bool);
                            """)


    create_table_queries = [create_trip_report_table, trip_location]

    for query in create_table_queries:
        cur.execute(query)
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