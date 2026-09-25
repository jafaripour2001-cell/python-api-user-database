import requests
import sqlite3

API_URL = "https://jsonplaceholder.typicode.com/users"
DB_NAME = "users.db"


def get_users():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("خطا در اتصال به API:", e)
        return None


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            city TEXT
        )
    """)

    connection.commit()
    connection.close()


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


def main():
    print("برنامه شروع شد")

    users = get_users()

    if users is None:
        print("دریافت اطلاعات انجام نشد.")
        return

    print("تعداد کاربران دریافت شده:", len(users))

    create_database()
    save_users(users)
    show_users()

    print("اطلاعات با موفقیت در SQLite ذخیره شد.")


if __name__ == "__main__":
    main()