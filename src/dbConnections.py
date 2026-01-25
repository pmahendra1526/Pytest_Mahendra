import pyodbc
import oracledb
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# print("Testing database connections...")
def oracle_connection():
    # dsn=os.getenv("ORACLE_DSN")
    # user=os.getenv("ORACLE_USERNAME")
    # password=os.getenv("ORACLE_PASSWORD")
    # print(f"DSN: {dsn}, User: {user}, Password: {password}")
    connection_string=os.getenv("ORACLE_CONNECTION_STRING")
    print("Oracle connection_string:", connection_string)
    try:
        connection = oracledb.connect(connection_string)
        print(f"Connection Successfull to Oracle")
        cursor = connection.cursor()
        return connection,cursor
    except Exception as e:
        print(f"Oracle connection test failed: {e}")
    # finally:
    #     if 'cursor' in locals():
    #         cursor.close()
    #     if 'connection' in locals():
    #         connection.close()


def sql_server_connection(): 
    connection_string = os.getenv("SQL_SERVER_CONNECTION_STRING")

    print("SQL Server connection_string:", connection_string)
    try:
        connection = pyodbc.connect(connection_string)
        print(f"Connection Successfull to SQL Server")
        cursor = connection.cursor()
        return connection,cursor
    except Exception as e:
        print(f"SQL Server connection test failed: {e}")
    # finally:
    #     if 'cursor' in locals():
    #         cursor.close()
    #     if 'connection' in locals():
    #         connection.close()


# sql_server_connection()
# oracle_connection()

# def fetch_table_data():
#     connection,cursor=sql_server_connection()
#     print("In fetch_table_data")
#     print(connection,cursor)
#     cursor.execute("SELECT * FROM EMPLOYEES")
#     columns = [desc[0] for desc in cursor.description]
#     data = [dict(zip(columns, row)) for row in cursor.fetchall()]
#     print(data)
#     if 'cursor' in locals():
#         cursor.close()
#     if 'connection' in locals():
#         connection.close()
    
# fetch_table_data()