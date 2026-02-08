import pytest
from src.dbConnections_fixture_parametrize import sql_server_connection,oracle_connection,execute_query
import pandas as pd

params_list=[('EMP_1','EMPLOYEES')]
# params_list=[('EMP_1','EMPLOYEES'),('EMP','EMPLOYEES')]


@pytest.mark.parametrize("sql_table,oracle_table",params_list)
def test_countCheck(execute_query,sql_table,oracle_table):
    print("In test_countCheck")
    sql_data,oracle_data=execute_query[0],execute_query[1]
    print(sql_data)
    print(oracle_data)
    assert len(sql_data)==len(oracle_data),f"SQL Count:{len(sql_data)}, Oracle Count:{len(oracle_data)}"

@pytest.mark.parametrize("sql_table,oracle_table",params_list)
def test_dataValidation(execute_query,sql_table,oracle_table):
    print("In test_dataValidation")
    sql_data,oracle_data=execute_query[0],execute_query[1]
    # 
    result=pd.merge(sql_data,oracle_data,how="outer",indicator=True)
    print("Result::\n",result)
    difference=result[result['_merge'] != 'both']
    print("Difference::\n",difference)
    assert difference.empty, "Data not matching."