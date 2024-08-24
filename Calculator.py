# Making a calculator

def add(*args):
    result = 0
    for num in args:
        result = result + num
    return result


def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result = result - num
    return result


def multiply(*args):
    result = 1
    for num in args:
        result = result * num
    return result


# In division, we can get zero error to address that issue we use try catch block

def divide(*args):
    try:
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."


def calculator(operation, *args):
    if operation == "addition" or "Addition":
        return add(*args)
    elif operation == "subtract" or "Subtract":
        return subtract(*args)
    elif operation == "multiply" or "Multiply":
        return multiply(*args)
    elif operation == "divide" or "Divide":
        return divide(*args)
    else:
        return ("Invalid operation. \n Please insert one of the following: \n 1.Addition \n 2.Subtract \n 3.Multiply "
                "\n 4.Divide")


operation = input("Enter the required operation:\n 1.Addition \n 2.Subtract \n 3.Multiply "
                  "\n 4.Divide \n")
no_of_input = input("Enter the number of inputs you want to operate on: ")

cal = []

for whatever in range(int(no_of_input)):
    number = input("Enter the number: ")
    cal.append(int(number)) #pushing numbers into array

final_result = calculator(operation, *cal)

print(f"The result of the operation is: {final_result}")

