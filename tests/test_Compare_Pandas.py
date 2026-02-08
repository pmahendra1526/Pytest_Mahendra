from src.dbConnections import *
from src.utils import convert_column_datatypes
import pandas as pd
import pytest

sql_query="SELECT * FROM EMP_1 order by EMPID asc"
oracle_query="SELECT * FROM EMPLOYEES WHERE EMPID IN(101,102) order by EMPID asc"

# @pytest.mark.data
def test_dataCompare_data_pandas():
    sql_data = execute_sql_query_pandas(sql_query)    
    oracle_data = execute_oracle_query_pandas(oracle_query)
    print("ORACLE DATA::",sql_data)
    print("ORACLE DATA::",oracle_data)
    # result=pd.merge(sql_data,oracle_data,how="outer",indicator=True)
    # differences=result[result['_merge'] != 'both']
    # print(differences)
    # assert len(differences)==0, "Data does not match between SQL Server and Oracle."
    assert sql_data.equals(oracle_data), "Data does not match between SQL Server and Oracle."

# @pytest.mark.count
def test_countCheck_pandas():
    sql_data = execute_sql_query_pandas(sql_query)
    oracle_data = execute_oracle_query_pandas(oracle_query)
    print(sql_data)
    print(oracle_data)
    assert len(sql_data) == len(oracle_data), f"Count mismatch: SQL Server has {len(sql_data)} rows, Oracle has {len(oracle_data)} rows." 

# @pytest.mark.schema
def test_schema_pandas():
    sql_data = execute_sql_query_pandas("SELECT COLUMN_NAME,DATA_TYPE,IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS \
                WHERE TABLE_NAME='EMP_1'")
    oracle_data = execute_oracle_query_pandas("SELECT COLUMN_NAME,DATA_TYPE,NULLABLE AS IS_NULLABLE FROM USER_TAB_COLUMNS WHERE TABLE_NAME='EMPLOYEES'")
    oracle_data = convert_column_datatypes(oracle_data)
    print(sql_data)
    print(oracle_data)
    result=pd.merge(sql_data,oracle_data,how="outer",indicator=True)
    differences=result[result['_merge'] != 'both']
    print(differences)
    assert len(differences)==0, "Schema Not Matching"




