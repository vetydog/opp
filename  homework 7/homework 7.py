class GeneratorIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration


def number_generator():
    for num in range(1, 6):
        yield num


iterator = GeneratorIterator(1, 5)


for num in iterator:
    print(num)


for num in number_generator():
    print(num)
