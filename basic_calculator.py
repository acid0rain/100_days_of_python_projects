from calc_art import logo

print(logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


# result = calc_operations['*'](4, 8)


def calculation(n1, operator, n2):
    if operator in calc_operations:
        result = ((calc_operations[operator](n1, n2)))
        print(f"Result: {result}")
        has_result = True
        return result, has_result

    else:
        print("Error. Please enter a valid operator symbol")
        return None


has_result = False
# calc loop
while True:
    if has_result:
        keepCalcing = input("Would you like to continue using the previous result? Y or N \n ").lower()
        if keepCalcing == "y":
            n1 = result
        else:
            n1 = int(input("Enter the first number: "))
    else:
        n1 = int(input("Enter the first number: "))

    operator = input(
        "Type the symbol for the operation you'd like: \n + Add \n - Subtract \n * Multiply \n / Divide \n")
    n2 = int(input("Enter the second number: "))

    result, has_result = calculation(n1, operator, n2)

    continue_calc = input("Would you like to do another calculation? Y or N \n").lower()
    if continue_calc != 'y':
        break
