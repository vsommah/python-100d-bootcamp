from art import logo


# Calculator

# Add
def add(n1, n2):
    """Add element 1 to element 2 and return value"""
    return n1 + n2


# Subtract
def subtract(n1, n2):
    """Subtract element 2 from element 1 and return value"""
    return n1 - n2


# Multiply
def multiply(n1, n2):
    """Multiply element 1 and element 2 and return value"""
    return n1 * n2


# Divide
def divide(n1, n2):
    """Divide element 1 by element 2 and return value"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# function = operations["+"]
# function(2,3)


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for operation in operations:
        print(operation)

    run_program = True

    while run_program:
        user_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation = operations[user_operation]
        answer = calculation(num1, num2)

        print(f"{num1} {user_operation} {num2} = {answer}")

        shall_continue = input(
            f"Type 'c' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'x' to exit: ")

        if shall_continue == "c":
            num1 = answer
        elif shall_continue == "n":
            run_program = False
            # Recursion of the function
            calculator()
        elif shall_continue == "x":
            print("Goodbye!")
            run_program = False


calculator()
