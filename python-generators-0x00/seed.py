import mysql.connector
import  csv
import uuid

# Connect to MySQL server
def connect_db():
    return mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password= 'database',
    )

# Create ALX_prodev database
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

# Connet to ALX_prodev database
def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="database",
        database="ALX_prodev"
    )
# Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR (36) Primary Key,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)      
        )
    """
    )
    connection.commit()
    cursor.close()

# Insert data from CSV
def insert_data(connection, csv_file):
    cursor = connection.cursor()

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row ['age']

            # Check for existing email before inserting
            cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
            if cursor.fetchone():
                continue
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """,(user_id, name, email, age))

    connection.commit()
    cursor.close()

def stream_users(connection):
    cursor = connection.cursor(buffered=False)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row
    cursor.close()

