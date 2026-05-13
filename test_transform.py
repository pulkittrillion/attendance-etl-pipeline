from extract import extract_data
from transform import transform_data

if __name__ == "__main__":
    # Extract
    df_raw = extract_data("data/raw/sample_attendance.csv")
    
    # Transform
    df_clean = transform_data(df_raw)
    
    print("\n✅ Transformed Data Preview:")
    print(df_clean.head())
    print("\nOvertime Summary:")
    print(df_clean[['employee_id', 'hours_worked', 'overtime_hours', 'compliance_flag']].head(10))