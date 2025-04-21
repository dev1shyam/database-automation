import pyodbc
from datetime import datetime, timedelta

# Connect to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=my_database;UID=sa;PWD=password')
cursor = conn.cursor()

# Define the cutoff date for cleanup (e.g., older than 6 months)
cutoff_date = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')

# Create the cleanup SQL command
cleanup_command = f"DELETE FROM logs WHERE log_date < '{cutoff_date}'"

# Execute the cleanup
cursor.execute(cleanup_command)
conn.commit()
print(f"Cleanup completed successfully for logs before {cutoff_date}")
conn.close()
