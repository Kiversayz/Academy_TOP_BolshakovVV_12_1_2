class RecipeController:
    fob = "Forbidden"
    user_owner = ['is_superpuper', 'is_staff', 'user_owner']
    is_staff = ['is_superpuper', 'is_staff']
    is_superpuper = ['is_superpuper']
    error_value = "Неверный тип данных - "

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return "Добро пожаловать в систему управления рецептами."

    def get_recipes_auth(self, role='guest'):
        """ Получить список рецептов с проверкой прав доступа. """
        if role in self.user_owner:
            if self.model.get_recipes():
                return self.model.get_recipes()
            return
        return self.fob

    def add_recipe_auth(self, name, author, recipe_type, description, ingredients, cuisine, youtube_link, file_name, role='guest'):
        """ Добавить рецепт с проверкой прав доступа. """
        if role not in self.is_superpuper and role not in self.is_staff:
            return self.fob
        elif not isinstance(name, str):
            return self.error_value + str(name)
        elif not isinstance(description, str):
            return self.error_value + str(description)
        return self.model.add_recipe(name, author, recipe_type, description, ingredients, cuisine, youtube_link, file_name)
