# import pyodbc
# import oracledb
# import os
# from dotenv import load_dotenv
# import pandas as pd
# import pytest

# # Load environment variables from .env file
# load_dotenv()

# # print("Testing database connections...")
# @pytest.fixture(scope="module")
# def oracle_connection():
#     # dsn=os.getenv("ORACLE_DSN")
#     # user=os.getenv("ORACLE_USERNAME")
#     # password=os.getenv("ORACLE_PASSWORD")
#     # print(f"DSN: {dsn}, User: {user}, Password: {password}")
#     connection_string=os.getenv("ORACLE_CONNECTION_STRING")
#     # print("Oracle connection_string:", connection_string)
#     try:
#         oracle_conn = oracledb.connect(connection_string)
#         print(f"Connection Successfull to Oracle")
#         oracle_cursor = oracle_conn.cursor()
#         yield oracle_conn,oracle_cursor
#         print("In Orcale Connections after yield")
#         oracle_conn.close()
#         oracle_cursor.close()
#     except Exception as e:
#         print(f"Oracle connection test failed: {e}")
#     # finally:
#     #     if 'cursor' in locals():
#     #         cursor.close()
#     #     if 'connection' in locals():
#     #         connection.close()

# @pytest.fixture(scope="module")
# def sql_server_connection(): 
#     connection_string = os.getenv("SQL_SERVER_CONNECTION_STRING")

#     # print("SQL Server connection_string:", connection_string)
#     try:
#         sql_conn = pyodbc.connect(connection_string)
#         print(f"Connection Successfull to SQL Server")
#         sql_cursor = sql_conn.cursor()
#         yield sql_conn,sql_cursor
#         print("In SQL Connections after yield")
#         sql_conn.close()
#         sql_cursor.close()
#     except Exception as e:
#         print(f"SQL Server connection test failed: {e}")
#     # finally:
#     #     if 'sql_cursor' in locals():
#     #         sql_cursor.close()
#     #     if 'sql_conn' in locals():
#     #         sql_conn.close()

# def close_connection():
#     pass

# @pytest.fixture(scope="module")
# def execute_query1(sql_server_connection,oracle_connection):
#     print("Test")
#     print(sql_server_connection[0],oracle_connection[0])
#     sql_conn=sql_server_connection[0]
#     oracle_conn=oracle_connection[0]
#     print(sql_conn)
#     print(oracle_conn)
#     # query=""
#     sql_df=pd.read_sql_query(f"Select * from EMP_1",sql_conn)
#     oracle_df=pd.read_sql_query(f"Select * from EMPLOYEES",oracle_conn)
#     print(sql_df)
#     print(oracle_df)
#     return sql_df,oracle_df