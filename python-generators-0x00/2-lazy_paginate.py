import seed

def paginate_users(page_size, offset):
    # Fetches one page of users starting from offset.
    conn = seed.connect_toprodev()
    cursor = conn.cursor()
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def lazy_paginate(page_size):
    #Generator that lazily paginates user_data using yield.
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

if __name__ == "__main__":
    for page in lazy_paginate(2):
        for user in page:
            print(user)

