import psycopg2
from psycopg2.extras import execute_values
import logging
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# Database config
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT")
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/etl.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def load_data(df, table_name="attendance"):
    """
    Load transformed data into PostgreSQL
    """
    logging.info(f"Starting load into table: {table_name}")
    
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            employee_id VARCHAR(50),
            date DATE,
            punch_in TIME,
            punch_out TIME,
            hours_worked NUMERIC(5,2),
            overtime_hours NUMERIC(5,2),
            branch VARCHAR(100),
            department VARCHAR(100),
            compliance_flag BOOLEAN,
            loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cur.execute(create_table_query)

        # Prepare data for loading
        df_load = df.copy()
        df_load['loaded_at'] = pd.Timestamp.now()   # optional

        # Convert DataFrame to list of tuples
        tuples = [tuple(x) for x in df_load.to_numpy()]

        # Insert data
        cols = ','.join(df_load.columns)
        insert_query = f"INSERT INTO {table_name} ({cols}) VALUES %s"
        
        execute_values(cur, insert_query, tuples)
        
        conn.commit()
        logging.info(f"✅ Successfully loaded {len(df)} records into {table_name} table")

        cur.close()
        conn.close()

    except Exception as e:
        logging.error(f"❌ Load failed: {str(e)}")
        raise