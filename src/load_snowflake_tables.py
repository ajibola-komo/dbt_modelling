import snowflake.connector
import os
from dotenv import load_dotenv
from src.paths import (TABLE_NAMES, STAGE_NAMES)
from src.envariables import(SNOWFLAKE_CONFIG)

load_dotenv()


def upload_from_s3_to_snowflake():

    conn = snowflake.connector.connect(
        **SNOWFLAKE_CONFIG
    )

    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE raw_hosts")
    cursor.execute("TRUNCATE TABLE raw_listings")
    cursor.execute("TRUNCATE TABLE raw_reviews")


    sql_stage = f"""
        CREATE OR REPLACE FILE FORMAT my_csv_format
            TYPE = 'csv'
            SKIP_HEADER = 1
            FIELD_OPTIONALLY_ENCLOSED_BY = '"'
            NULL_IF = ('NULL', '');
"""
    
    cursor.execute(sql_stage)

    sql = f"""
    CREATE STAGE IF NOT EXISTS airbnb_stage
    URL='s3://dbt-datasets/'
    FILE_FORMAT=(FORMAT_NAME = 'my_csv_format');
"""
    cursor.execute(sql)

    cursor.execute(f"""
        COPY INTO raw_hosts
        FROM @airbnb_stage
        FILES = ('hosts.csv')
        FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
        """)
    
    cursor.execute(f"""
        COPY INTO raw_listings
        FROM @airbnb_stage
        FILES = ('listings.csv')
        FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
        """)
    
    cursor.execute(f"""
        COPY INTO raw_reviews
        FROM @airbnb_stage
        FILES = ('reviews.csv')
        FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
        """)

    
    cursor.close()
    conn.close()



