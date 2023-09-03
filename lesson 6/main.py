import warnings
'''
try:
    your_code #requests, database, arythmetic proccess... 
except ...:
    proc_error/exception
'''
'''
while(True):
    try:
        digit1 = 10
        #warnings.warn("\nPossible zero division!\n")
        digit2 = int(input("Enter digit: "))
        res = digit1/digit2
        print(res)
    except ZeroDivisionError as zde:
        print(f"Custom proccess: {zde}")
    except Exception as ex:
        print(ex)
    yes = input("Enter Y for continue or N for stop: ")
    if(yes.lower() == "n"):
        break
print("Cycle while has stoped!")
'''
from buildingerror import BuildingError
from validation import Validation
limit = 10
amount = int(input("Enter amount: "))
check = Validation(amount, limit)
try:
    Validation(amount, limit).Check()
    #check.Check()
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde}")
except BuildingError as be:
    print(f"Custom error message\n"
          f"{be}")
except Exception as ex:
    print(ex)
