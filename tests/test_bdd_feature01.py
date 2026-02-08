from pytest_bdd import scenario,given,when,then,scenarios,feature
import pytest
from src.dbConnections_fixtures import oracle_connection,sql_server_connection,execute_query_count

FEATURE_FILE=r"D:\MyProjects\Pytest_Mahendra\src\bdd_pytest\features\feature01.feature"
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

@when("Get records count from SQL server table 'EMP_1' and Oracle table 'EMPLOYEES'")
def get_records_count(execute_query_count):
    print("get_records_count")
    sql_count,oracle_count=execute_query_count
    row_count["sql_count"]=sql_count[0]
    row_count["oracle_count"]=oracle_count[0]
    print(row_count)

@then("Records count should match")
def compare_records_count():
    assert row_count['sql_count']==row_count['oracle_count'],f"Count not matching. SQL Count is {row_count['sql_count']}, Oracle count is {row_count['oracle_count']}"




