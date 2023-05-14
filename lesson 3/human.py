'''
t or f = t
f or t = t
t or t = t
f or f = f
t and t = t
t and f = f
f and t = f
f and f = f
'''
class Human:

    def __init__(self, name, role):
        self.Name = name
        self.Role = role

    def ToString(self):
        print(f"Name: {self.Name}\n"
              f"Role: {self.Role}")