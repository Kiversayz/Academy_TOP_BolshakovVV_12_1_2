class RecipeView:
    fob = "Forbidden"

    def __init__(self, controller):
        self.controller = controller

    def display_default_action(self):
        print(self.controller.get_default_action())

    def display_recipes_auth(self, role='guest'):
        """ Отобразить список рецептов с проверкой прав доступа. """
        result = self.controller.get_recipes_auth(role)
        if result == self.fob:
            print(self.fob)
            return
        if result:
            for recipe in result:
                print(f'Рецепт: {recipe["name"]}, Автор: {recipe["author"]}, Тип: {recipe["recipe_type"]}')
            return
        print('Рецептов нет.')
    
    def post_add_recipe_auth(self, name, author, recipe_type, description, ingredients, cuisine, youtube_link, file_name, role='guest'):
        """ Добавить рецепт с проверкой прав доступа. """
        result = self.controller.add_recipe_auth(name, author, recipe_type, description, ingredients, cuisine, youtube_link, file_name, role)
        if result == True:
            print(f'Рецепт "{name}" от {author} успешно добавлен.')
        elif result == False:
            print(f'Рецепт "{name}" уже существует.')
        elif result == self.fob:
            print("У вас недостаточно прав доступа.")