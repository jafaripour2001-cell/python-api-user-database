import sqlite3


DB_NAME = "users.db"


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            city TEXT
        )
    """)

    connection.commit()
    connection.close()


def database_is_empty():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    connection.close()

    return count == 0


def save_users(users):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    for user in users:
        cursor.execute("""
            INSERT OR REPLACE INTO users
            (id, name, username, email, city)
            VALUES (?, ?, ?, ?, ?)
        """, (
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["address"]["city"]
        ))

    connection.commit()
    connection.close()


def show_users():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, username, email, city
        FROM users
    """)

    users = cursor.fetchall()

    connection.close()

    print("\nفهرست کاربران ذخیره شده در SQLite:")

    for user in users:
        print("--------------------")
        print("ID:", user[0])
        print("نام:", user[1])
        print("نام کاربری:", user[2])
        print("ایمیل:", user[3])
        print("شهر:", user[4])


def update_user():
    user_id = input("\nشناسه کاربر را وارد کنید: ")
    new_email = input("ایمیل جدید را وارد کنید: ")

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET email = ?
        WHERE id = ?
    """, (new_email, user_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("کاربری با این شناسه پیدا نشد.")
    else:
        print("ایمیل کاربر با موفقیت تغییر کرد.")

    connection.close()


def delete_user():
    user_id = input("\nشناسه کاربری که می‌خواهید حذف کنید: ")

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE id = ?
    """, (user_id,))

    connection.commit()

    if cursor.rowcount == 0:
        print("کاربری با این شناسه پیدا نشد.")
    else:
        print("کاربر با موفقیت از دیتابیس حذف شد.")

    connection.close()