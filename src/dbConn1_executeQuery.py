from src.dbConnections_1 import sql_server_connection,oracle_connection
import pandas as pd

def execute_query(sql_table,oracle_table):
    print("Test")
    print(sql_table,oracle_table)
    sql_conn=sql_server_connection()[0]
    oracle_conn=oracle_connection()[0]
    print(sql_conn)
    print(oracle_conn)
    # query=""
    sql_df=pd.read_sql_query(f"Select * from {sql_table}",sql_conn)
    oracle_df=pd.read_sql_query(f"Select * from {oracle_table}",oracle_conn)
    print(sql_df)
    print(oracle_df)
    return sql_df,oracle_df
    pass

execute_query('EMP_1','EMPLOYEES')