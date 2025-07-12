import seed
from decimal import Decimal, getcontext

def stream_user_ages():
    # Yields user ages one by one from user data table.
    conn = seed.connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield Decimal(age)

    cursor.close()
    conn.close()

def compute_average_age():
    # Calculates and prints the average age using the generator.
    total = Decimal(0)
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        avg = total / count
        print(f"Average age of users: {avg:.2f}")
    else:
        print("No users found.")

if __name__ == "__main__":
    compute_average_age()