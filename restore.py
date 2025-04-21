import pyodbc

# Connect to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=password')
cursor = conn.cursor()

# Define the backup file to restore from
backup_file = "C:/backups/DB_Backup_20230415123000.bak"

# Create the restore SQL command
restore_command = f"RESTORE DATABASE my_database FROM DISK = '{backup_file}'"

# Execute the restore
cursor.execute(restore_command)
conn.commit()
print(f"Restore completed successfully from {backup_file}")
conn.close()
