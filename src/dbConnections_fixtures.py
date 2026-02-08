import pyodbc
import oracledb
import os
from dotenv import load_dotenv
import pandas as pd
import pytest

# Load environment variables from .env file
load_dotenv()

# print("Testing database connections...")
@pytest.fixture(scope="module")
def oracle_connection():
    connection_string=os.getenv("ORACLE_CONNECTION_STRING")
    print("Oracle connection_string:", connection_string)
    try:
        oracle_conn = oracledb.connect(connection_string)
        print(f"Connection Successfull to Oracle")
        yield oracle_conn
        print("In Orcale Connections after yield")
    except Exception as e:
        print(f"Oracle connection test failed: {e}")
        return None
    # finally:
    #     if 'oracle_conn' in locals():
    #         oracle_conn.close()
    #     print("Oracle Connection Closed")

@pytest.fixture(scope="module")
def sql_server_connection(): 
    connection_string = os.getenv("SQL_SERVER_CONNECTION_STRING")
    print("SQL Server connection_string:", connection_string)
    try:
        sql_conn = pyodbc.connect(connection_string)
        print(f"Connection Successfull to SQL Server")
        yield sql_conn
        print("In SQL Connections after yield")
    except Exception as e:
        print(f"SQL Server connection test failed: {e}")
        return None
    # finally:
    #     if 'sql_conn' in locals():
    #         sql_conn.close()
    #     print("SQL Connection Closed")

def close_connection():
    pass

@pytest.fixture(scope="module")
def execute_query(sql_conn=sql_server_connection,oracle_conn=oracle_connection):
    # print("Test")
    # print(sql_server_connection,oracle_connection)
    # sql_conn=sql_server_connection[0]
    # oracle_conn=oracle_connection[0]
    # print(sql_conn)
    # print(oracle_conn)
    # query=""
    sql_df=pd.read_sql_query(f"Select * from EMP_1",sql_conn)
    oracle_df=pd.read_sql_query(f"Select * from EMPLOYEES",oracle_conn)
    print(sql_df)
    print(oracle_df)
    return sql_df,oracle_df

@pytest.fixture(scope="module")
def execute_query_count(sql_server_connection,oracle_connection):
    sql_cursor,oralce_cursor=sql_server_connection.cursor(),oracle_connection.cursor()
    sql_cursor=sql_cursor.execute(f"Select count(*) as count from EMP_1")
    oralce_cursor=oralce_cursor.execute(f"Select count(*) as count from EMPLOYEES")
    sql_count=sql_cursor.fetchone()
    oracle_count=oralce_cursor.fetchone()
    return sql_count,oracle_count

@pytest.fixture(scope="module")
def execute_query_data(sql_server_connection,oracle_connection):
    sql_cursor,oralce_cursor=sql_server_connection.cursor(),oracle_connection.cursor()
    sql_df=sql_cursor.execute(f"Select * from EMP_1")
    oracle_df=oralce_cursor.execute(f"Select * from EMPLOYEES")
    print(sql_df)
    print(oracle_df)
    return sql_df,oracle_df

@pytest.fixture(scope="module")
def execute_query_count1(sql_server_connection,oracle_connection):
    print("In execute_query_count1")
    sql_cursor,oralce_cursor=sql_server_connection.cursor(),oracle_connection.cursor()
    # sql_cursor=sql_cursor.execute(f"Select count(*) as count from {sql_table}")
    # oralce_cursor=oralce_cursor.execute(f"Select count(*) as count from {oracle_table}")
    # sql_count=sql_cursor.fetchone()
    # oracle_count=oralce_cursor.fetchone()
    return sql_cursor,oralce_cursor

# def test_query(execute_query1):
#     print("In Test Query")
#     sql_data,oracle_data=execute_query1[0],execute_query1[1]
#     print(sql_data)
#     print(oracle_data)
#     assert len(sql_data)==len(oracle_data),f"SQL Count:{len(sql_data)}, Oracle Count:{len(oracle_data)}"



# execute_query1(sql_server_connection)

# def execute_sql_query_pandas(query):
#     sql_conn,sql_cursor= sql_server_connection()
#     try:
#         sql_data = pd.read_sql_query(query, sql_conn)
#         return sql_data
#     except Exception as e:
#         print(f"Query execution failed: {e}")
#         return None
    
# def execute_oracle_query_pandas(query):
#     oracle_conn,oracle_cursor= oracle_connection()
#     try:
#         oracle_data = pd.read_sql_query(query, oracle_conn)
#         return oracle_data
#     except Exception as e:
#         print(f"Query execution failed: {e}")
#         return None

# def execute_sql_query_cursor(query):
#     sql_conn,sql_cursor= sql_server_connection()
#     try:
#         sql_cursor.execute(query)
#         data = sql_cursor.fetchall()
#         print("sql_cursor Fetch All::",data)
#         print("sql_cursor Description::",sql_cursor.description)
#         columns = [desc[0] for desc in sql_cursor.description]
#         # sql_data = [{columns[i]: row[i] for i in range(len(columns))} for row in data]
#         sql_data = [dict(zip(columns, row)) for row in data] 
#         # or below code
#         # oracle_data = [{columns[i]: row[i] for i in range(len(columns))} for row in data]
#         return sql_data
#     except Exception as e:
#         print(f"Query execution failed: {e}")
#         return None

# def execute_oracle_query_cursor(query):
#     oracle_conn,oracle_cursor= oracle_connection()
#     try:
#         oracle_cursor.execute(query)
#         data = oracle_cursor.fetchall()
#         columns = [desc[0] for desc in oracle_cursor.description]
#         oracle_data = [{columns[i]: row[i] for i in range(len(columns))} for row in data]
#         # oracle_data = [dict(zip(columns, row)) for row in data]#  
#         return oracle_data
#     except Exception as e:
#         print(f"Query execution failed: {e}")
#         return None


# connection,cursor=execute_sql_query_cursor("SELECT * FROM EMP_1 order by 1")
# print(connection,cursor)

# sql_server_connection(sql_server_connection)
# oracle_connection()