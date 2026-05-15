from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":
    print(" Starting Full ETL Test...\n")
    
    # Extract
    df_raw = extract_data("data/raw/sample_attendance.csv")
    
    # Transform
    df_clean = transform_data(df_raw)
    
    # Load
    load_data(df_clean)
    
    print("\n Full ETL Pipeline executed successfully!")
    print("Check the 'attendance' table in pgAdmin to see the loaded data.")