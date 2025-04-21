import pyodbc
from datetime import datetime

# Connect to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=password')
cursor = conn.cursor()

# Define backup file path
backup_file = f"C:/backups/DB_Backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"

# Create the backup SQL command
backup_command = f"BACKUP DATABASE my_database TO DISK = '{backup_file}'"

# Execute the backup
cursor.execute(backup_command)
conn.commit()
print(f"Backup completed successfully: {backup_file}")
conn.close()
