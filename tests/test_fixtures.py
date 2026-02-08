import pytest
from src.dbConnections_fixture import sql_server_connection,oracle_connection,execute_query
import pandas as pd

def test_countCheck(execute_query):
    print("In test_countCheck")
    sql_data,oracle_data=execute_query[0],execute_query[1]
    print(sql_data)
    print(oracle_data)
    assert len(sql_data)==len(oracle_data),f"SQL Count:{len(sql_data)}, Oracle Count:{len(oracle_data)}"

def test_dataValidation(execute_query):
    print("In test_dataValidation")
    sql_data,oracle_data=execute_query[0],execute_query[1]
    # 
    result=pd.merge(sql_data,oracle_data,how="outer",indicator=True)
    difference=result[result['_merge'] != 'both']
    print(difference)
    assert difference.empty, "Data not matching."