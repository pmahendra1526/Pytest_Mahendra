import pyodbc
import oracledb
import os
from dotenv import load_dotenv
import pytest

# Load environment variables from .env file
load_dotenv()

# print("Testing database connections...")
def test_oracle_connection():
    dsn=os.getenv("ORACLE_DSN")
    user=os.getenv("ORACLE_USERNAME")
    password=os.getenv("ORACLE_PASSWORD")
    print(f"DSN: {dsn}, User: {user}, Password: {password}")
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM EMPLOYEES")
        print(cursor.description)
        columns=[col[0] for col in cursor.description]
        print(columns)
        # print(cursor.fetchall())
        # data=[row for row in cursor.fetchall()]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print(data)
        result = cursor.fetchone()
        assert result[0] == 1
        print("Oracle connection test passed.")
    except Exception as e:
        print(f"Oracle connection test failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


test_oracle_connection()

def test_sql_server_connection(): 
    connection_string = os.getenv("SQL_SERVER_CONNECTION_STRING")
    print(connection_string)
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        assert result[0] == 1
        print("SQL Server connection test passed.")
    except Exception as e:
        print(f"SQL Server connection test failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

test_sql_server_connection()


# # list=[(101, 'John Doe', 50000.0), (102, 'Jane Smith', None), (103, 'Peter Jones', 60000.0), (104, 'Mary Williams', 55000.0)]
# # # # res=dict(zip(['EMPID', 'EMPNAME', 'SALARY'],list) )
# # columns=['EMPID', 'EMPNAME', 'SALARY']
# # res=[dict(zip(columns,list)) for list in list]
# # print(res)

# # data = [dict(zip(['EMPID', 'EMPNAME', 'SALARY'], row)) for row in list]
# # print(data)

# print("Test Data")
# res=zip(['EMPID', 'EMPNAME', 'SALARY'],(102, 'Jane Smith', 200))

# # print(dict(res))

# # print(list(res))
# print(dict(res))