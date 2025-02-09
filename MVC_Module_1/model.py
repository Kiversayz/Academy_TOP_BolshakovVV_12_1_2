import json

class Shoe:
    def __init__(self):
        """Создание класса для хранения данных об обуви."""
        self.__shoes = []

    def get_shoes(self):
        """Получить список всех обувных товаров."""
        return self.__shoes

    def add_shoe(self, shoe_type, shoe_kind, color, price, manufacturer, size, file_name):
        """Добавить обувь в список."""
        if not self.check_shoe(shoe_type, shoe_kind, size):
            data = {
                'type': shoe_type,
                'kind': shoe_kind,
                'color': color,
                'price': price,
                'manufacturer': manufacturer,
                'size': size
            }
            self.__shoes.append(data)
            self.update_json(file_name)
            return True
        else:
            return False

    def check_shoe(self, shoe_type, shoe_kind, size):
        """Проверка, существует ли обувь с такими характеристиками."""
        for shoe in self.__shoes:
            if shoe['type'] == shoe_type and shoe['kind'] == shoe_kind and shoe['size'] == size:
                return True
        return False

    def update_json(self, file_name):
        """Обновить файл с данными об обуви."""
        full_file_name = fr'MVC_Module_1\file\{file_name}_shoe_data.json'
        with open(full_file_name, 'w', encoding='utf-8') as fp:
            json.dump(self.__shoes, fp, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    shoe_model = Shoe()

    shoe_model.add_shoe('Мужская', 'Кроссовки', 'Черный', 5000, 'Nike', 42, 'shoes')
    shoe_model.add_shoe('Женская', 'Сапоги', 'Красный', 8000, 'Adidas', 37, 'shoes')

    print(shoe_model.get_shoes())

