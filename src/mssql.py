import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};SERVER=localhost,1433;UID=sa;PWD=yourStrong(!)Password')
cursor = cnxn.cursor()

print('Using the following SQL Server version:')
tsql = "SELECT @@version;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    print(str(row[0]))