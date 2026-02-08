from pytest_bdd import scenario,given,when,then,scenarios,feature,parsers
import pytest
from src.dbConnections_fixtures import oracle_connection,sql_server_connection,execute_query_count1

FEATURE_FILE=r"D:\MyProjects\Pytest_Mahendra\src\bdd_pytest\features\feature02.feature"
print(FEATURE_FILE)
print("Mahendra")

row_count={}

# # --- Scenario Definition ---
@scenario(FEATURE_FILE,"Compare records count between SQL Server and Oracle")
def test_records_count():
    print("test_records_count")

@given("Have access to SQL Server and Oracle server")
def check_connections(sql_server_connection,oracle_connection):
    print("check_connections::",sql_server_connection,oracle_connection)
    assert sql_server_connection is not None and oracle_connection is not None, "DB Connections Failed"

@when(parsers.parse('Get records count from SQL server table "{sql_table}" and Oracle table "{oracle_table}"'))
def get_records_count(execute_query_count1,sql_table,oracle_table):
    print("get_records_count")
    sql_cursor,oralce_cursor=execute_query_count1
    sql_cursor=sql_cursor.execute(f"Select count(*) as count from {sql_table}")
    oralce_cursor=oralce_cursor.execute(f"Select count(*) as count from {oracle_table}")
    sql_count=sql_cursor.fetchone()
    oracle_count=oralce_cursor.fetchone()
    row_count["sql_count"]=sql_count[0]
    row_count["oracle_count"]=oracle_count[0]
    print(row_count)

@then("Records count should match")
def compare_records_count():
    assert row_count['sql_count']==row_count['oracle_count'],f"Count not matching. SQL Count is {row_count['sql_count']}, Oracle count is {row_count['oracle_count']}"





