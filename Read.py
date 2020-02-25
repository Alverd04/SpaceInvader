import pyodbc

conn = pyodbc.connect(
    "Driver = {SQL Server Native Client 11.0};"
    "Server =;"
    "Database =;"
    "Trusted_Connection=yes;"
)