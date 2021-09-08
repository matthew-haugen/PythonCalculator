#################################
#-------------------------------#
#--- Basic Python Calculator ---#
#-------------------------------#
#################################

### Imports ###
import math
from mpmath import *

### Definitions ###
#Adding two numbers
def add(x, y):
    return x + y

#Subtracting two numbers
def sub(x, y):
    return x - y

#Multiplying two numbers
def mul(x, y):
    return x * y

#Dividing two numbers
def div(x, y):
    return x / y

#Exponent of two numbers
def pow(x, y):
    return x**y

#Percentage of two numbers
def per(x, y):
    return x / y * 100

#Logarithm of two numbers
def log(x, y):
    return math.log(x, y)

#Natural Logarithm
def nlog(x):
    return math.log(x)

#Sine
def sin(x):
    return math.sin(x)

#Cosine
def cos(x):
    return math.cos(x)

#Tangent
def tan(x):
    return math.tan(x)

### Troubleshooting Messages ###
#Error Message
errMessage = "Invalid Input. Please try again."

### External Framework ###
print("Select an operation: \n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponents")
print("6. Percentage (x / y)")
print("7. Logarithm Base")
print("8. Natural Logarithm" )
print("9. Sine")
print("9b. Cosecant")
print("10. Cosine")
print("10b. Secant")
print("11. Tangent")
print("11b. Cotangent \n")

### Application Logic ###
while True:
    #User Input
    select = input("Enter selection (1-11): ")
    num1 = float(input("Enter first number: "))

    #Check if selection is valid and if selection 8
    if select in ('8','9','10','11'):
        if select == '8':
            print("Natural logarithm of ", num1, " is ", nlog(num1))
        
        if select == '9':
            print("sin(", num1,")=",sin(num1))
        
        if select == '10':
            print("cos(", num1,")=",cos(num1))
        
        if select == '11':
            print("tan(", num1,")=",tan(num1))

        break

    else:
        #Check if selection is valid and if selection 1-6
        if select in ('1','2','3','4','5','6','7'):
            num2 = float(input("Enter second number: "))

            if select == '1':
                print(num1, "+", num2, "=", add(num1,num2))
            
            elif select == '2':
                print(num1, "-", num2,"=", sub(num1,num2))

            elif select == '3':
                print(num1, "*", num2, "=", mul(num1,num2))

            elif select == '4':
                print(num1, "/", num2, "=", div(num1,num2))

            elif select == '5':
                print(num1, "^", num2, "=", pow(num1,num2))
            
            elif select == '6':
                print(num1, "/", num2, "=", per(num1,num2),"%")

            elif select == '7':
                print("Logarithm base ", num1, " of ", num2, "is: ", log(num2,num1))
            
            break
        
        else:
            print(errMessage)