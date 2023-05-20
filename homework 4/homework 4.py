import random

class HiddenNumber:
    def __init__(self, number):
        self.hidden_number = number

    def __str__(self):
        result = self.hidden_number
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            result += random.randint(1, 10)
        elif operation == '-':
            result -= random.randint(1, 10)
        elif operation == '*':
            result *= random.randint(2, 5)
        elif operation == '/':
            result /= random.randint(2, 5)

        return str(result)


number = HiddenNumber(42)
print(number)  #
print(number)
