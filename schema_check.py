import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('theater.db')
cursor = conn.cursor()

# Query to get table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Query to get schema for 'roles' table
cursor.execute("PRAGMA table_info(roles);")
roles_schema = cursor.fetchall()
print("Roles Table Schema:")
for column in roles_schema:
    print(column)

# Query to get schema for 'auditions' table
cursor.execute("PRAGMA table_info(auditions);")
auditions_schema = cursor.fetchall()
print("Auditions Table Schema:")
for column in auditions_schema:
    print(column)

# Close the connection
conn.close()
