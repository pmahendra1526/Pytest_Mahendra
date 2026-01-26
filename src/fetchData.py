from dbConnections import sql_server_connection, oracle_connection

def sql_query_fetch(query):
    connection, cursor = sql_server_connection()
    try:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data
    except Exception as e:
        print(f"Query execution failed: {e}")
        return None

def oracle_query_fetch(query):
    connection, cursor = oracle_connection()
    try:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data
    except Exception as e:
        print(f"Query execution failed: {e}")
        return None
    
# Example usage:
# dATA SHOULD BE IN SAME ORDER FOR COMPARISON
sql_data = sql_query_fetch("SELECT * FROM EMP_1") 
oracle_data = oracle_query_fetch("SELECT * FROM EMPLOYEES where empid IN(101,102)")
print(sql_data)
print(oracle_data)

# def test_compare_data(sql_data, oracle_data):
#     if sql_data not in oracle_data or oracle_data not in sql_data:
#         print("Data does not match between SQL Server and Oracle.")
#         return
#     print("Data matches between SQL Server and Oracle.")

# if sql_data==oracle_data:
#     print("Data matches between SQL Server and Oracle.")
# else:
#     print("Data does not match between SQL Server and Oracle.")

# def compare_data(sql_data, oracle_data):
#     if len(sql_data) != len(oracle_data):
#         print(f"Data length mismatch: SQL Server has {len(sql_data)} rows, Oracle has {len(oracle_data)} rows.")
#         return
#     for i in range(len(sql_data)):
#         if sql_data[i] != oracle_data[i]:
#             print(f"Mismatch found at row {i}:\nSQL Server: {sql_data[i]}\nOracle: {oracle_data[i]}")
#             return
#     print("Data matches between SQL Server and Oracle.")
#    for sql_row, oracle_row in zip(sql_data, oracle_data):
#        if sql_row != oracle_row:
#            print(f"Mismatch found:\nSQL Server: {sql_row}\nOracle: {oracle_row}")
#            return
   
# compare_data(sql_data, oracle_data)