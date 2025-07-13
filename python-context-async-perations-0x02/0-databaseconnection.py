import mysql.connector

class DatabaseConnection:
    # Custom context manager for MySQL connections
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    with DatabaseConnection(
        host="locahost",
        user="root",
        password="database",
        database="ALX_prodev"
    ) as cursor:
        cursor.execute("SELECT * FROM user_data")
        results = cursor.fetchall()
        for row in results:
            print(row)