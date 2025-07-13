import mysql.connector

class ExecuteQuery:
    # Custom context manager to execute a parameterised query.
    def __init__(self, query,params):
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="database",
            database="ALX_prodev"
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close

if __name__ == "__main__":
    query = "SELECT * FROM user_data WHERE age > %s"
    param = (25,)

    with ExecuteQuery(query, param) as results:
        for row in results:
            print(row)