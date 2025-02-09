from MVC import controller
from MVC import model
from MVC import viwe

def main():
    mod = model.Timetable()
    control = controller.TimetamleController(mod)
    vi = viwe.TimeViwe(control)

    vi.display_def_action()

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть расписание (авторизация)")
        print("2. Просмотреть все курсы и даты")
        print("3. Добавить курс (авторизация)")
        print("4. Изменить дату курса (авторизация)")
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            role = input("Введите вашу роль (guest, is_staff, is_superpuper, user_owner): ")
            vi.display_times_auth(role)
        elif choice == '2':
            vi.display_all_times()
        elif choice == '3':
            role = input("Введите вашу роль (guest, is_staff, is_superpuper, user_owner): ")
            course = input("Название курса: ")
            month_day = input("Дата (например, 15 Марта): ")
            file_name = input("Имя файла для сохранения: ")
            vi.post_add_time_auth(course, month_day, file_name, role)
        elif choice == '4':
            role = input("Введите вашу роль (guest, is_staff, is_superpuper, user_owner): ")
            course = input("Название курса: ")
            month_day = input("Новая дата (например, 20 Апреля): ")
            file_name = input("Имя файла для сохранения: ")
            vi.post_update_time_course_auth(course, month_day, file_name, role)
        elif choice == '5':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()