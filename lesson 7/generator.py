from iteration import Iteration
class Generator(Iteration) :
    def __init__(self, i = 0 ):
        super().__init__(i)
    def Raise_to_the_degrees_F(self , number , max_degree):
        for _ in range(max_degree) :
            yield  number ** self.I
            self.I +=1

    def Raise_to_the_degrees_W(self, number, max_degree):
        while(True):
            if(self.I > 500):
                break
                yield  number ** self.I
                self.I += 1
