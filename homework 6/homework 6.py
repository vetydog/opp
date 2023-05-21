import traceback
import sys

result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError as ve:
        print("ValueError occurred:", ve)
    except IndexError as ie:
        print("IndexError occurred:", ie)
    except Exception as e:
        print("An unexpected error occurred:", e)
        traceback.print_exc()
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data.get(key))
    if res is not None:
        result.append(res)

print(result)
