from MVC_Module_2 import controller
from MVC_Module_2 import model
from MVC_Module_2 import viwe

def main():
    mod = model.Recipe()
    control = controller.RecipeController(mod)
    vi = viwe.RecipeView(control)

    vi.display_default_action()

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть рецепты (авторизация)")
        print("2. Добавить рецепт (авторизация)")
        print("3. Exit")

        choice = input("Ваш выбор:")

        if choice == '1':
            role = input("Введите свою роль (guest, is_staff, is_superpuper, user_owner): ")
            vi.display_recipes_auth(role)
        elif choice == '2':
            role = input("Введите свою роль (guest, is_staff, is_superpuper, user_owner): ")
            name = input("Название рецепта: ")
            author = input("Автор: ")
            recipe_type = input("Тип рецепта (первый, второй и т.д.): ")
            description = input("Описание:")
            ingredients = input("Ингредиенты (через запятую):").split(", ")
            cuisine = input("Кухня: ")
            youtube_link = input("Ссылка на YouTube (необязательно):")
            file_name = input("Имя файла для сохранения:")
            vi.post_add_recipe_auth(name, author, recipe_type, description, ingredients, cuisine, youtube_link, file_name, role)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()