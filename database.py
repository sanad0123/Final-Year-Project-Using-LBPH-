import mysql.connector
import project_standard as ps

# Connect to the MySQL server
cnx = mysql.connector.connect(user=ps.username, password=ps.password, host=ps.host)

# Create a cursor object
cursor = cnx.cursor()

# Execute the SHOW DATABASES statement
cursor.execute("SHOW DATABASES")

# Get the list of databases
databases = cursor.fetchall()

# Check if the desired database exists
database_exists = False
for database in databases:
    if ps.db in database:
        database_exists = True
        break

if database_exists:
    cnx = mysql.connector.connect(user=ps.username, password=ps.password,
                              host=ps.host, database=ps.db)
    cursor = cnx.cursor()

    table_name = ps.table

    query = "SHOW TABLES LIKE '{}'".format(table_name)
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Database and Table exists")
    else:
        # Execute the CREATE TABLE statement
        cursor.execute(
            "CREATE TABLE student ( Dep VARCHAR(255), Course VARCHAR(255), Year VARCHAR(255), Sem VARCHAR(255),ID INT PRIMARY KEY, Name VARCHAR(255), Sec VARCHAR(255), Roll VARCHAR(255), Gender VARCHAR(255), DOB VARCHAR(255), Email VARCHAR(255), Phone VARCHAR(255), Address VARCHAR(255), Teacher VARCHAR(255), Photo VARCHAR(255))")
    
else:
    # Execute the CREATE DATABASE statement
    cursor.execute("CREATE DATABASE smartattendancesystem")

    # Select the database
    cursor.execute("USE smartattendancesystem")

    # Execute the CREATE TABLE statement
    cursor.execute(
        "CREATE TABLE student ( Dep VARCHAR(255), Course VARCHAR(255), Year VARCHAR(255), Sem VARCHAR(255),ID INT PRIMARY KEY, Name VARCHAR(255), Sec VARCHAR(255), Roll VARCHAR(255), Gender VARCHAR(255), DOB VARCHAR(255), Email VARCHAR(255), Phone VARCHAR(255), Address VARCHAR(255), Teacher VARCHAR(255), Photo VARCHAR(255))")

    # Commit the changes
    cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()