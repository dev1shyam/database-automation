import pyodbc
import logging

# Set up logging
logging.basicConfig(filename='db_automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to the database
try:
    logging.info("Starting the restore process.")
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=password')
    cursor = conn.cursor()

    # Define the backup file to restore from
    backup_file = "C:/backups/DB_Backup_20230415123000.bak"

    # Create the restore SQL command
    restore_command = f"RESTORE DATABASE my_database FROM DISK = '{backup_file}'"

    # Execute the restore
    cursor.execute(restore_command)
    conn.commit()
    
    logging.info(f"Restore completed successfully from {backup_file}")

except Exception as e:
    # Log error
    logging.error(f"Error occurred during restore: {str(e)}")

finally:
    # Ensure connection is closed
    if 'conn' in locals():
        conn.close()
        logging.info("Database connection closed.")
