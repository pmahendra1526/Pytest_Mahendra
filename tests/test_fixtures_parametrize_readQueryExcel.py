import pytest
from src.dbConnections_fixture_parametrize_readQueryExcel import sql_server_connection,oracle_connection,execute_query
import pandas as pd
from src.utils import read_spreadsheet

params_list_count,ids_list_count,params_list_DataCheck,ids_list_data=read_spreadsheet()
# params_list_count=[x for x in params_list if x[0]=="Count_Check"]
# params_list_count=[tup[1:] for tup in params_list_count]
# params_list_DataCheck=[x for x in params_list if x[0]=="Data_Validation"]
# params_list_DataCheck=[tup[1:] for tup in params_list_DataCheck]

print(params_list_count)
print()
print(params_list_DataCheck)


@pytest.mark.parametrize("sql_query,oracle_query",params_list_count,ids=ids_list_count)
def test_countCheck(execute_query,sql_query,oracle_query):
    print("In test_countCheck")
    sql_data,oracle_data=execute_query[0],execute_query[1]
    print(sql_data)
    print(oracle_data)
    assert len(sql_data)==len(oracle_data),f"SQL Count:{len(sql_data)}, Oracle Count:{len(oracle_data)}"

@pytest.mark.parametrize("sql_query,oracle_query",params_list_DataCheck,ids=ids_list_data)
def test_dataValidation(execute_query,sql_query,oracle_query):
    print("In test_dataValidation")
    sql_data,oracle_data=execute_query[0],execute_query[1]
    # 
    result=pd.merge(sql_data,oracle_data,how="outer",indicator=True)
    print("Result::\n",result)
    difference=result[result['_merge'] != 'both']
    print("Difference::\n",difference)
    assert difference.empty, "Data not matching."