class Human:
    def __init__(self,name,age,height):
        self.Name = name
        self.Age = age
        self.Height = height


    def __str__(self):
        return f"Name: {self.Name}\nAge: {self.Age}\nHeight: {self.Height}\n"

