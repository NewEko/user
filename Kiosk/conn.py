import pyodbc
server = 'mssql-157657-0.cloudclusters.net, 16555'
database = 'db_system'
username = 'root_db'
password = 'newUser09112001'
# Create a connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


try:
    # Attempt to establish the connection
    connection = pyodbc.connect(connection_string)

    # If no exception is raised, the connection is successful
    print("Connected to the database!")

    # Create a cursor
    cursor = connection.cursor()

    # Execute a simple query to further verify the connection
    cursor.execute('SELECT * from tbl_users')

    # Fetch the result
    result = cursor.fetchall()
    for row in result:
        print(row)

except Exception as e:
    # Handle any exceptions that may occur during connection
    print(f"Error connecting to the database: {e}")

finally:
    # Close the connection in the 'finally' block to ensure it's closed
    if connection:
        connection.close()
        print("Connection closed.")