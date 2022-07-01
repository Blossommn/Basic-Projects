# Simple Calculator
# 1. ADDITION
# 2. SUBTRACTION
# 3. MULTIPLICATION
# 4. DIVISION

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    #code for add
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    sum = int(str(num1)) + int(str(num2))
    print("The sum is " + str(float(sum)) )
elif operation == "2":
    #code for subtract

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    minuend = int(str(num1)) - int(str(num2))
    print("The difference is " + str(float(minuend)))

elif operation == "3":
    #code for multiply
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    multiple = int(str(num1)) * int(str(num2))
    print("The product is " + str(float(multiple)))

elif operation == "4":
    #code for dividing
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    dividend = int(str(num1)) / int(str(num2))
    print("The dividend is " + str(float(dividend)))
else:
    print("Invalid Entry")