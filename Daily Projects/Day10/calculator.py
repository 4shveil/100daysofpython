from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

first_number = float(input("What is the first number for the calculation: "))
while True:
    input_operation = input("What would you like to do? ('+', '-', '*', '/'.: ")
    if input_operation not in operations:
        print("Invalid input. Please try again.")
        continue
    second_number = float(input("What is the second number for the calculation: "))
    print(f"{first_number} {input_operation} {second_number}")
    first_number = operations[input_operation](first_number, second_number)
    print(f"Result: {first_number}")
    if input("Continue? (y/n): ").lower().startswith('n'):
        print("Thank you for choosing pypy Calculator cya!")
        break
    print(f"Continuing with previous result of the calculation...: {first_number}")
