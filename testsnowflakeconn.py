import pandas as pd
import snowflake.connector
con = snowflake.connector.connect(
    user='Shiv.Singh@stada.de',
    account='OZ58375.west-europe.privatelink', #
    role='PROD_DH_HQ_ESO_READ', # Your role
    authenticator='externalbrowser'
)



# Create a cursor
cursor = con.cursor()

# Execute a SELECT query
query = 'SELECT * FROM PROD_DH.HQ_ESO_CONTROL.ESO_OTIF LIMIT1'  # Replace with your actual table name
cursor.execute(query)

# Fetch the one row
result = cursor.fetchone()

# Get the column names
column_names = [desc[0] for desc in cursor.description]

# Display the column names
print("Column Names:", column_names)

# Display the one row of data
print("Data:", result)

# Close the cursor and connection
cursor.close()
con.close()