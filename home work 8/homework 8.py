import time
import unittest

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time



def sample_function(n):

    return sum(range(1, n + 1))

class TestMeasureTime(unittest.TestCase):
    def test_measure_time(self):
        result, execution_time = measure_time(sample_function, 1000000)
        self.assertEqual(result, 500000500000)  # Очікуваний результат
        self.assertGreater(execution_time, 0)  # Час виконання має бути більше 0

if __name__ == '__main__':
    unittest.main()
