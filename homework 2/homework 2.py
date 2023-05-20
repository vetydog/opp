import time

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.age = 0
        self.is_sleeping = False
        self.hunger_level = 0

    def sleep(self):
        if not self.is_sleeping:
            self.is_sleeping = True
            print(f"{self.name} засыпает...")
            time.sleep(2)
            print(f"{self.name} просыпается.")
            self.is_sleeping = False
        else:
            print(f"{self.name} уже спит.")

    def eat(self):
        if not self.is_sleeping:
            if self.hunger_level > 0:
                self.hunger_level -= 1
                print(f"{self.name} ест. Уровень голода: {self.hunger_level}")
            else:
                print(f"{self.name} не голоден.")
        else:
            print(f"{self.name} спит и не может есть.")

    def play(self):
        if not self.is_sleeping:
            print(f"{self.name} играет и веселится!")
        else:
            print(f"{self.name} спит и не может играть.")

    def age_one_year(self):
        self.age += 1
        print(f"С днем рождения, {self.name}! Теперь ему {self.age} год(а).")

dog = Dog("Бобик", "Дворняжка")
dog.sleep()
dog.eat()
dog.play()
dog.age_one_year()
