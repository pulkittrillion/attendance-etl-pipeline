from extract import extract_data
from transform import transform_data
from load import load_data
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/etl.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    print("="*60)
    print("😎🚀 Starting Attendance ETL Pipeline")
    print("="*60)
    
    try:
        # Step 1: Extract
        logging.info("=== Starting ETL Pipeline ===")
        df_raw = extract_data("data/raw/sample_attendance.csv")
        
        # Step 2: Transform
        df_clean = transform_data(df_raw)
        
        # Step 3: Load
        load_data(df_clean)
        
        print("\n🎉 SUCCESS: Full ETL Pipeline Completed Successfully!")
        print(f"   → Loaded {len(df_clean)} records into database")
        
    except Exception as e:
        print(f"\n❌ Pipeline Failed: {e}")
        logging.error(f"Pipeline failed: {e}")
    
    print("="*60)