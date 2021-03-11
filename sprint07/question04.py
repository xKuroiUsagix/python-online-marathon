class Washing:
    @staticmethod
    def wash():
        print('Washing...')


class Rinsing:
    @staticmethod
    def rinse():
        print('Rinsing...')


class Spinning:
    @staticmethod
    def spin():
        print('Spinning...')


class WashingMachine:
    def __init__(self) -> None:
        self.wash = Washing.wash
        self.rinse = Rinsing.rinse
        self.spin = Spinning.spin
        self.startWashing()

    
    def startWashing(self):
        self.wash()
        self.rinse()
        self.spin()