print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation: "))

if(option in [1, 2,3,4]):
    num1 = int(input("Enter First number"))
    num2 = int(input("Enter Second number"))


    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif (option == 3):
        result = num1 * num2
    elif (option == 4):
        result = num1 // num2
else:
    print("invalid operation entered")

print("the result of the operation is {}".format(result))