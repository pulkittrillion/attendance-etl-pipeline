# Attendance ETL Pipeline



\*\*End-to-end automated ETL pipeline\*\* for processing employee attendance data in a large-scale cash logistics company (99+ branches).



\## Business Problem

Previously, attendance reporting was done manually in Excel, which was time-consuming and error-prone. This pipeline automates the entire process — from raw data to clean database — saving hours of manual work every month.



\## Tech Stack

\- Python 3

\- Pandas (Data Manipulation)

\- PostgreSQL (Database)

\- psycopg2 (Database Connector)

\- Logging \& Error Handling



\## Project Structure



├── extract.py

├── transform.py

├── load.py

├── main.py

├── config.py

├── queries.sql

├── data/raw/

└── README.md

## Pipeline Architecture
1. **Extract** → Read raw CSV data
2. **Transform** → Clean data + calculate hours, overtime, compliance
3. **Load** → Store in PostgreSQL database

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run full pipeline
python main.py



\## Features (In Progress)

\- \[ ] Data Extraction from CSV/Excel

\- \[ ] Data Cleaning \& Transformation

\- \[ ] Load to PostgreSQL

\- \[ ] Logging \& Monitoring

\- \[ ] Business Metrics (Overtime, Compliance)



\*\*Status\*\*: In Development



\---

