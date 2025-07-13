import sqlite3

class DatabaseConnection:
    # Custom context manager to manage SQLite connection
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    db_path = "users.db"

    with DatabaseConnection(db_path) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)