from src.create_snowflake_tables import create_raw_tables
from dotenv import load_dotenv
from src.load_snowflake_tables import upload_from_s3_to_snowflake
from src.run_dbt import run_dbt_models

load_dotenv()

def run_pipeline():
    create_raw_tables()
    upload_from_s3_to_snowflake()
    run_dbt_models()


run_pipeline()