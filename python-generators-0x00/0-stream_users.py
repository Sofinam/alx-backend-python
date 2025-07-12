import seed

# Connect and create DB
conn = seed.connect_db()
seed.create_database(conn)
conn.close()

# Connect to ALX_prodev and create table
conn = seed.connect_to_prodev()
seed.create_table(conn)
seed.insert_data(conn, 'user_data.csv')

def stream_users():
    cursor = conn.cursor(buffered=False)
    cursor.execute("SELECT * FROM user_data")

    # Created a loop
    for row in cursor:
        yield row
    cursor.close()

for user in stream_users():
    print(user)

conn.close()



    