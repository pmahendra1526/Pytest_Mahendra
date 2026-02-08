Feature: Comapare SQL and Oracle Data
    Validate scenarios Count Check, Schema Check, Data Validation & Duplicate Checks

    Scenario: Compare records count between SQL Server and Oracle 
        Given Have access to SQL Server and Oracle server
        When Get records count from SQL server table 'EMP_1' and Oracle table 'EMPLOYEES'
        Then Records count should match