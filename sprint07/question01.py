from abc import abstractmethod


class Product:
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    name = 'Fettuccine Alfredo'

    def cook(self):
        print(f'Italian main course prepared: {self.name}')


class Tiramisu(Product):
    name = 'Tiramisu'

    def cook(self):
        print(f'Italian dessert prepared: {self.name}')


class DuckALOrange(Product):
    name = "Duck À L'Orange"

    def cook(self):
        print(f'French main course prepared: {self.name}')


class CremeBrulee(Product):
    name = "Crème brûlée"

    def cook(self):
        print(f'French dessert prepared: {self.name}')


class Factory:
    @abstractmethod
    def get_dish(meal_type):
        pass


class ItalianDishesFactory(Factory):
    @staticmethod
    def get_dish(meal_type):
        return Tiramisu() if meal_type == 'dessert' else FettuccineAlfredo()


class FrenchDishesFactory(Factory):
    @staticmethod
    def get_dish(meal_type):
        return CremeBrulee() if meal_type == 'dessert' else DuckALOrange()


class FactoryProducer:
    @staticmethod
    def get_factory(factory_type):
        return ItalianDishesFactory() if factory_type == 'italian' else FrenchDishesFactory()