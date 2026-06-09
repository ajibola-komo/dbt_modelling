from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DDL_DIR = PROJECT_ROOT / "sql"



BRONZE_TABLE_PATHS = [
    DDL_DIR / "raw_listings.sql", DDL_DIR / "raw_reviews.sql", DDL_DIR / "raw_hosts.sql"
]

DATABASE_NAME = "AIRBNB"

SCHEMA_NAME = "AIRBNB.bronze"

TABLE_NAMES = ["raw_reviews.sql","raw_hosts", "raw_listings"]

STAGE_NAMES = ["hosts_stage","reviews_stage","listings_stage"]