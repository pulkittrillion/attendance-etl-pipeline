import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raw attendance data: clean + calculate key metrics
    """
    logging.info("Starting data transformation...")

    try:
        df = df.copy()

        # 1. Basic Cleaning
        df = df.drop_duplicates()
        df = df.dropna(subset=['employee_id', 'date', 'punch_in', 'punch_out'])

        # 2. Convert Date (Flexible parsing)
        df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

        # 3. Convert Time columns
        df['punch_in'] = pd.to_datetime(df['punch_in'], format='%H:%M', errors='coerce').dt.time
        df['punch_out'] = pd.to_datetime(df['punch_out'], format='%H:%M', errors='coerce').dt.time

        # Remove rows where date/time conversion failed
        df = df.dropna(subset=['date', 'punch_in', 'punch_out'])

        # 4. Calculate Hours Worked and Overtime
        def calculate_hours(row):
            in_time = datetime.combine(datetime.min, row['punch_in'])
            out_time = datetime.combine(datetime.min, row['punch_out'])
            hours = (out_time - in_time).total_seconds() / 3600
            overtime = max(0, hours - 9)
            return pd.Series({
                'hours_worked': round(hours, 2),
                'overtime_hours': round(overtime, 2)
            })

        df = df.join(df.apply(calculate_hours, axis=1))

        # 5. Add Compliance Flag
        df['compliance_flag'] = df['hours_worked'] >= 8

        logging.info(f"✅ Transformation completed. Final records: {len(df)}")
        return df

    except Exception as e:
        logging.error(f"❌ Transformation failed: {str(e)}")
        raise