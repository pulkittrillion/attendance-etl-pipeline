import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    print("✅ Successfully connected to PostgreSQL!")
    
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print("PostgreSQL version:", cur.fetchone()[0])
    
    cur.close()
    conn.close()
    print("✅ Connection test completed successfully!")

except Exception as e:
    print("❌ Error:", e)