import seed
from decimal import Decimal

def stream_users_in_batches(batch_size):
    # Generator that yields rows from user_data in batches.
    conn = seed.connect_to_prodev()
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch
    cursor.close()
    conn.close()

def batch_processing():
    # Process batches to filter users over age 25.
    for batch in stream_users_in_batches(3):
        over_25 = [user for user in batch if Decimal(user[3]) > 25]
        for user in over_25:
            print(user)

if __name__ == '__main__':
    batch_processing()