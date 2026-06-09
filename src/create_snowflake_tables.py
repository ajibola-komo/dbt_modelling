from src.envariables import SNOWFLAKE_CONFIG
import snowflake.connector
from src.paths import DDL_DIR, BRONZE_TABLE_PATHS, DATABASE_NAME, SCHEMA_NAME
from dotenv import load_dotenv

load_dotenv()



def create_raw_tables():
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = conn.cursor()

    cursor.execute(F'''USE DATABASE {DATABASE_NAME}''')
    cursor.execute(f'''USE SCHEMA {SCHEMA_NAME}''')

    for ddl_path in BRONZE_TABLE_PATHS:

        sql_path = ddl_path
        with open(sql_path, "r") as f:
            ddl = f.read()
        
        cursor.execute(ddl)

    cursor.close()
    conn.close()
    

