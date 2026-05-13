from extract import extract_data

if __name__ == "__main__":
    df = extract_data("data/raw/sample_attendance.csv")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData Info:")
    print(df.info())