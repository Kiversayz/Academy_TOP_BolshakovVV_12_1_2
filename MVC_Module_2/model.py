import json

class Recipe:
    def __init__(self):
        """ Создание класса с контейнером для хранения данных о рецептах. """
        self.__recipes = []

    def get_recipes(self):
        """ Получить список рецептов. """
        return self.__recipes

    def add_recipe(self, name, author, recipe_type, description, ingredients, cuisine, youtube_link, file_name):
        """ Добавить новый рецепт. """
        if not self.check_recipe(name):
            data = {
                'name': name,
                'author': author,
                'recipe_type': recipe_type,
                'description': description,
                'ingredients': ingredients,
                'cuisine': cuisine,
                'youtube_link': youtube_link
            }
            self.__recipes.append(data)
            self.update_json(file_name)
            return True
        return False

    def check_recipe(self, name):
        """ Проверить, существует ли рецепт с таким названием. """
        for recipe in self.__recipes:
            if recipe['name'] == name:
                return True
        return False

    def update_json(self, file_name):
        """ Обновить файл с рецептом. """
        full_file_name = fr'MVC_Module_2/file/{file_name}_recipes.json'
        with open(full_file_name, 'w', encoding='utf-8') as fp:
            json.dump(self.__recipes, fp, ensure_ascii=False, indent=4)