from src.dbConnections import *
# from src.fetchData import sql_query_fetch, oracle_query_fetch
import pandas as pd
import pytest

sql_query="SELECT * FROM EMP_1 order by 1"
oracle_query="SELECT * FROM EMPLOYEES WHERE EMPID IN(101,102) order by 1"

@pytest.mark.data
def test_dataCompare_data_cursor():
    sql_data = execute_sql_query_cursor(sql_query)
    oracle_data = execute_oracle_query_cursor(oracle_query)
    print(sql_data)
    print(oracle_data)
    assert sql_data == oracle_data, "Data does not match between SQL Server and Oracle."   

@pytest.mark.count
def test_countCheck_cursor():
    sql_data = execute_sql_query_cursor(sql_query)
    oracle_data = execute_oracle_query_cursor(oracle_query)
    print(sql_data)
    print(oracle_data)
    assert len(sql_data) == len(oracle_data), f"Count mismatch: SQL Server has {len(sql_data)} rows, Oracle has {len(oracle_data)} rows."   

