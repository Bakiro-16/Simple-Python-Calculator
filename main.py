#The functions.
def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Welcome to Calculator")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


while 3 != 2:
    operation = input('Select the operation you want to perform (1/2/3/4): ')
    if operation in ("1", "2", "3", "4"):
        num1 = float(input('Insert the first number of your mathematical problem here ====>'))
        num2 = float(input('Insert the second number of your mathematical problem here ====>'))
        if operation == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation == "2":
            print(num1, "-", num2, '=', minus(num1, num2))
        elif operation == "3":
            print(num1, "*", num2, '=', multiply(num1, num2))
        elif operation == "4":
            print(num1, "/", num2, '=', divide(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            input("Thanks for using!")
            break


    else:
        print("Invalid input.")



