class ShoeController:
    fob = "Forbidden"
    user_owner = ['is_superpuper', 'is_staff', 'user_owner']
    is_staff = ['is_superpuper', 'is_staff']
    is_superpuper = ['is_superpuper']
    error_value = "Неверный тип данных - "

    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return "Добро пожаловать в магазин обуви."

    def get_shoes_auth(self, role='guest'):
        if role in self.user_owner:
            if self.model.get_shoes():
                return self.model.get_shoes()
            return
        return self.fob

    def get_only_shoe_types(self):
        shoe_types = []
        data = self.model.get_shoes()
        if data:
            for shoe in data:
                shoe_types.append(shoe['type'])
            return shoe_types
        return

    def add_shoe_auth(self, shoe_type, shoe_kind, color, price, manufacturer, size, file_name, role='guest'):
        if role not in self.is_superpuper and role not in self.is_staff:
            return self.fob
        return self.model.add_shoe(shoe_type, shoe_kind, color, price, manufacturer, size, file_name)


