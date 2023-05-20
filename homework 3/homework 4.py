class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model}: Включение устройства.")


class Phone(Device):
    def __init__(self, brand, model, phone_number):
        super().__init__(brand, model)
        self.phone_number = phone_number

    def make_call(self, number):
        print(f"{self.brand} {self.model}: Вызываю номер {number}...")


class Tablet(Device):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def play_game(self, game):
        print(f"{self.brand} {self.model}: Запускаю игру {game}.")


phone = Phone("Apple", "iPhone 12", "123-456-789")
tablet = Tablet("Samsung", "Galaxy Tab S7")

phone.power_on()
phone.make_call("987-654-321")

tablet.power_on()
tablet.play_game("Angry Birds")
