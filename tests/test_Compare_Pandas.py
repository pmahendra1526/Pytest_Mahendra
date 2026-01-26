from src.dbConnections import *
# from src.fetchData import sql_query_fetch, oracle_query_fetch
import pandas as pd
import pytest


sql_query="SELECT * FROM EMP_1 order by 1"
oracle_query="SELECT * FROM EMPLOYEES WHERE EMPID IN(101,102) order by 1"

@pytest.mark.skip
def test_dataCompare_data_pandas():
    sql_data = execute_sql_query_pandas("SELECT * FROM EMP_1 order by 1")    
    oracle_data = execute_oracle_query_pandas("SELECT * FROM EMPLOYEES WHERE EMPID IN(101,102) order by 1")
    print(sql_data)
    print(oracle_data)
    assert sql_data.equals(oracle_data), "Data does not match between SQL Server and Oracle."

@pytest.mark.skip
def test_countCheck_pandas():
    sql_data = execute_sql_query_pandas(sql_query)
    oracle_data = execute_oracle_query_pandas(oracle_query)
    print(sql_data)
    print(oracle_data)
    assert len(sql_data) == len(oracle_data), f"Count mismatch: SQL Server has {len(sql_data)} rows, Oracle has {len(oracle_data)+1} rows." 


def test_schema_pandas():
    sql_data = execute_sql_query_pandas("SELECT COLUMN_NAME,DATA_TYPE,IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS \
                WHERE TABLE_NAME='EMP_1'")
    oracle_data = execute_oracle_query_pandas("SELECT COLUMN_NAME,DATA_TYPE,NULLABLE FROM USER_TAB_COLUMNS WHERE TABLE_NAME='EMPLOYEES'")
    print(sql_data)
    print(oracle_data)
    assert len(sql_data) == len(oracle_data), f"Count mismatch: SQL Server has {len(sql_data)} rows, Oracle has {len(oracle_data)+1} rows." 