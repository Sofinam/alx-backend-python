import aiosqlite
import asyncio

DB_FILE = "users.db"
async def async_fetch_users():
    #fetch all users
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM user_data") as cursor:
            rows = await  cursor.fetchall()
            print("All Users:")
            for row in rows:
                print(row)
async def async_fetch_older_users():
    #fetch users older than 40
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM user_data WHERE age > 40") as cursor:
            rows = await cursor.fetchall()
            print("\nUsers older than 40:")
            for row in rows:
                print(row)
async def fetch_concurrently():
    # Run both fetches at the same time.
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())