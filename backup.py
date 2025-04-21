import pyodbc
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='db_automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to the database
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=password')
    cursor = conn.cursor()

    # Define backup file path
    backup_file = f"C:/backups/DB_Backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"

    # Create the backup SQL command
    backup_command = f"BACKUP DATABASE my_database TO DISK = '{backup_file}'"

    # Execute the backup
    cursor.execute(backup_command)
    conn.commit()
    
    # Log success
    logging.info(f"Backup completed successfully: {backup_file}")

except Exception as e:
    # Log error
    logging.error(f"Error occurred: {str(e)}")

finally:
    # Ensure connection is closed
    if 'conn' in locals():
        conn.close()
