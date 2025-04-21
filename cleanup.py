import pyodbc
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(filename='db_automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to the database
try:
    logging.info("Starting the cleanup process.")
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=my_database;UID=sa;PWD=password')
    cursor = conn.cursor()

    # Define the cutoff date for cleanup (e.g., older than 6 months)
    cutoff_date = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')

    # Create the cleanup SQL command
    cleanup_command = f"DELETE FROM logs WHERE log_date < '{cutoff_date}'"

    # Execute the cleanup
    cursor.execute(cleanup_command)
    conn.commit()
    
    logging.info(f"Cleanup completed successfully for logs before {cutoff_date}")

except Exception as e:
    # Log error
    logging.error(f"Error occurred during cleanup: {str(e)}")

finally:
    # Ensure connection is closed
    if 'conn' in locals():
        conn.close()
        logging.info("Database connection closed.")
