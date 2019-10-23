import math

while 1 == 1:
    print("Enter 'add' to add two number")
    print("Enter 'mul' to multiply two number")
    print("Enter 'div' to divide two number")
    print("Enter 'sub' to subtract two number")
    print("Enter 'sq' to square a number")
    print("Enter 's' to get the square root of a number")
    print("Enter 'quit' to end the program")
    number = input(" ")

    if number == "add":
        num1 = int(input("Enter a valid number"))
        num2 = int(input("Enter another number"))
        total1 = str(num1 + num2)
        print('The total number is ' + total)
