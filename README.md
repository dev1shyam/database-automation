# Database Automation System

This project automates common database tasks, including backups, restores, and data cleanup. It uses Python to run SQL commands for SQL Server (or Oracle) and logs the execution details.

## 🚀 Project Setup

### 1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/database-automation.git
   cd database-automation
```

### 2. Install Dependencies:
Make sure you have Python and the required libraries installed. You’ll need pyodbc for SQL Server (or cx_Oracle for Oracle).

```
pip install pyodbc
```

### 3. Configure Database Connection:

In each script, update the connection string to match your database configuration.

Example for SQL Server:

```
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=password')
```

### 4. Run the scripts:

Backup - python backup.py <br>
Restore - python restore.py <br>
Cleanup - python cleanup.py <br>

### 5. Automate the scripts:

Automate the scipts by adding it in the cron job

## Logs
All script executions are logged in db_automation.log. You can check this log to view the details of each execution, including success or any errors. The log file is automatically generated in the root directory of the project.

Log Levels: <br>
INFO: Script started, completed, or successful actions. <br>
ERROR: Issues encountered during script execution. <br>
