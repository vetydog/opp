
from human import Human
from speak import Speak

class ItStepStundet(Human,Speak):
    def __init__(self,name,age,height, group,avgGrade):
        super().__init__(name,age,height)
        self.Group = group
        self.AvgGrade = avgGrade
        self.SayName(name)
    def __str__(self):
        return f"{super().__str__()}Group : {self.Group}\nAcg grade: {self.AvgGrade}"
