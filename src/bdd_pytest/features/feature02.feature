Feature: Comapare SQL and Oracle Data
    Validate scenarios Count Check, Schema Check, Data Validation & Duplicate Checks

    Background: SQL and Oracle Connections Check
        Given Have access to SQL Server and Oracle server
    Scenario Outline: Compare records count between SQL Server and Oracle 
        When Get records count from SQL server table "<sql_table>" and Oracle table "<oracle_table>"
        Then Records count should match

        Examples:
            | sql_table     | oracle_table  |
            | EMP_1         | EMPLOYEES     |
            | EMP           | EMPLOYEES     |
            | EMPLOYEES     | EMPLOYEES     |
        