import pyodbc

dsn = 'mongo_housing'
try:
    # Connect to your database using the DSN
    connection = pyodbc.connect(f'DSN={dsn}', autocommit=True)
    
    # If successful, print a success message
    print("Connected successfully to the database.")
    
    # Perform a simple query to test the connection
    # Ensure you have a table/view set up that corresponds to your MongoDB collection
    cursor = connection.cursor()
    # Example query: replace 'your_collection' with an actual collection/table name
    cursor.execute("SELECT * FROM your_collection LIMIT 1")
    row = cursor.fetchone()
    if row:
        print("Query executed successfully:", row)
    
    # Close the connection
    connection.close()
except Exception as e:
    # If connection fails, print an error message
    print("Failed to connect to the database:", str(e))
