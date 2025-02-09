from MVC_Module_1.controller import ShoeController
from MVC_Module_1.model import Shoe
from MVC_Module_1.viwe import ShoeView

def main():
    shoe_model = Shoe()
    shoe_controller = ShoeController(shoe_model)
    shoe_view = ShoeView(shoe_controller)

    shoe_view.display_default_action()

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть обувь (авторизация)")
        print("2. Добавить обувь (авторизация)")
        print("3. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            role = input("Введите вашу роль (guest, is_staff, is_superpuper, user_owner): ")
            shoe_view.display_shoes_auth(role)
        elif choice == '2':
            role = input("Введите вашу роль (guest, is_staff, is_superpuper, user_owner): ")
            shoe_type = input("Тип обуви (мужская/женская): ")
            shoe_kind = input("Вид обуви: ")
            color = input("Цвет обуви: ")
            price = input("Цена: ")
            manufacturer = input("Производитель: ")
            size = int(input("Размер обуви: "))
            file_name = input("Имя файла для сохранения: ")
            shoe_view.post_add_shoe_auth(shoe_type, shoe_kind, color, price, manufacturer, size, file_name, role)
        elif choice == '3':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()