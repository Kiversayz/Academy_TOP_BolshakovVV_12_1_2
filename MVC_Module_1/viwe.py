class ShoeView:
    fob = "Forbidden"

    def __init__(self, controller):
        self.controller = controller

    def display_default_action(self):
        print(self.controller.get_default_action())

    def display_shoes_auth(self, role='guest'):
        result = self.controller.get_shoes_auth(role)
        if result == self.fob:
            print(self.fob)
            return
        if result:
            for item in result:
                print(f'{item["type"]} - {item["kind"]}: {item["color"]}, {item["price"]}₽, Производитель: {item["manufacturer"]}, Размер: {item["size"]}')
            return
        print('Нет доступной информации об обуви.')

    def post_add_shoe_auth(self, shoe_type, shoe_kind, color, price, manufacturer, size, file_name, role='guest'):
        result = self.controller.add_shoe_auth(shoe_type, shoe_kind, color, price, manufacturer, size, file_name, role)
        if result == True:
            print(f'Обувь: {shoe_type} - {shoe_kind} успешно добавлена.')
        elif result == self.fob:
            print("У вас недостаточно прав доступа.")


