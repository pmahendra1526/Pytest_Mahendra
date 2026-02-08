import pytest
from src.dbConn1_executeQuery import execute_query

@pytest.mark.parametrize("sql_table,oracle_table", 
                         [('EMP_1','EMPLOYEES'),('EMP','EMPLOYEES'),
                          ('EMPLOYEES','EMPLOYEES')])
def test_count_check(sql_table,oracle_table):
    sql_df,oracle_df=execute_query(sql_table,oracle_table)
    assert len(sql_df)==len(oracle_df),f"SQL table {sql_table} count: {len(sql_df)} ,Oracle table {oracle_table} count: {len(oracle_df)}"
