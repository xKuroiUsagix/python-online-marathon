class Pizza:
    orders = 0

    def __init__(self, ingredients: list) -> None:
        self.ingredients = ingredients
        self.order_number = Pizza.orders + 1
        Pizza.orders += 1


    @staticmethod
    def hawaiian():
        return Pizza(['ham', 'pineapple'])


    @staticmethod
    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])


    @staticmethod
    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])