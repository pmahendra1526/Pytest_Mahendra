import pyodbc
import oracledb
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# print("Testing database connections...")
def oracle_connection():
    dsn=os.getenv("ORACLE_DSN")
    user=os.getenv("ORACLE_USERNAME")
    password=os.getenv("ORACLE_PASSWORD")
    print(f"DSN: {dsn}, User: {user}, Password: {password}")
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        print(f"Connection Successfull to Oracle")
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM EMPLOYEES")
        result = cursor.fetchone()
        print(result[0])
        return result,cursor
    except Exception as e:
        print(f"Oracle connection test failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

oracle_connection()

def sql_server_connection(): 
    connection_string = os.getenv("SQL_SERVER_CONNECTION_STRING")

    print(connection_string)
    try:
        connection = pyodbc.connect(connection_string)
        print(f"Connection Successfull to SQL Server")
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print(f"SQL Server connection test failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

sql_server_connection()

