import pandas as pd
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract attendance data from CSV or Excel file.
    """
    try:
        logging.info(f"Starting extraction from: {file_path}")
        
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Read the file
        if file_path.suffix.lower() == '.csv':
            df = pd.read_csv(file_path)
        elif file_path.suffix.lower() in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")
        
        logging.info(f"✅ Successfully extracted {len(df)} records with {len(df.columns)} columns")
        logging.info(f"Columns: {list(df.columns)}")
        
        return df
        
    except Exception as e:
        logging.error(f"❌ Extraction failed: {str(e)}")
        raise