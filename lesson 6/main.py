import warnings
'''
while(True):
 try :
     digit1 = 10
     digit2 = int(input("Enter digit : "))
     #warnings.warn("\nPossible zero division")
     res = digit1/digit2
     print(res)

 except ZeroDivisionError as zde :
    print(f" Cudtom process : {zde}")
 except Exception as ex:
    print(ex)
 y = input("Enter Y for coninue or N for stop")
 if(y.lower() == "n") :
     break
'''
from buildingerror import BuildingError
from validation import Validation
limit = 10
amount = int(input("Enter amount: "))
check = Validation(amount, limit)
try:
 check.Check()
except ZeroDivisionError as zde:
 print(f"ZeroDivisionError: {zde}")
except BuildingError as be:
 print(f"Custom error message\n"
f"{be}")
except Exception as ex:
 print(ex)




