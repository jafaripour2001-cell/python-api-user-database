from api import get_users
from database import (
    create_database,
    database_is_empty,
    save_users,
    show_users,
    update_user,
    delete_user
)


def database_menu():
    while True:
        print("\n===== مدیریت دیتابیس =====")
        print("1. نمایش کاربران")
        print("2. تغییر ایمیل کاربر")
        print("3. حذف کاربر")
        print("4. خروج")

        choice = input("گزینه مورد نظر را وارد کنید: ")

        if choice == "1":
            show_users()

        elif choice == "2":
            update_user()

        elif choice == "3":
            delete_user()

        elif choice == "4":
            print("برنامه به پایان رسید.")
            break

        else:
            print("گزینه نامعتبر است.")


def main():
    print("برنامه شروع شد")

    create_database()

    if database_is_empty():
        print("دیتابیس خالی است؛ دریافت اطلاعات از API...")

        users = get_users()

        if users is None:
            print("دریافت اطلاعات انجام نشد.")
            return

        print("تعداد کاربران دریافت شده:", len(users))

        save_users(users)

    else:
        print("اطلاعات از قبل در دیتابیس وجود دارد.")

    database_menu()


if __name__ == "__main__":
    main()