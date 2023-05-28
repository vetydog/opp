from counter import Counter
from generator import Generator
'''
name = "Andrii"
#for i in iter(name):
    #print(i)
try :
     iterator = iter(name)
     print(next(iterator))
     print(next(iterator))
     print(next(iterator))
     print(next(iterator))
     print(next(iterator))
     print(next(iterator))
     print(next(iterator))
except StopIteration :
    print("Stop iteration")
    '''
'''
#Counter
counter = Counter(9)
for i  in counter :
    print(i)
    '''
generator = Generator(0)
res = generator.Raise_to_the_degrees_F(122345,500)
print(res)
for item in generator.Raise_to_the_degrees_F(122345,500):
    print(f"{item}\n")