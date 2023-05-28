from logging import DEBUG, basicConfig, debug, info, warning, error, critical
basicConfig(level= DEBUG,
filename='lesson8log.log',
filemode='a',
format="We have next logging message: %(asctime)s : %(levelname)s - %(message)s")
def IntSum(a, b):
    strDigit1 = str(a)
    strDigit2 = str(b)
    if(strDigit1.isdigit() and strDigit2.isdigit()):
        return int(float(a) + float(b))
'''
if(IntSum(5, 7.2) == 12):
print("True")
else:
print("False")
'''
while(True):
    try:
        digit1 = input("Enter digit1: ")
        digit2 = input("Enter digit2: ")
        assert IntSum(digit1, digit2) == 12, f"digit1: {digit1} + digit2: {digit2} != 12"
    except AssertionError as ae:
        error(ae)
    finally:
        yes = input("Enter Y for continue or N for stop: ")
    if(yes.lower() == "n"):
        break
