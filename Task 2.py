# Function to sum two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Function to divide two numbers
def divide_numbers(a, b):
    return a / b

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    # Getting user's operation choice
    operation = input("Enter option (1/2/3/4): ")

    # Ensuring valid operation choice
    if operation in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operation == '1':
            print(f"{number1} + {number2} = {add_numbers(number1, number2)}")

        elif operation == '2':
            print(f"{number1} - {number2} = {subtract_numbers(number1, number2)}")

        elif operation == '3':
            print(f"{number1} * {number2} = {multiply_numbers(number1, number2)}")

        elif operation == '4':
            if number2 == 0:
                print("Error: Division by zero is undefined.")
            else:
                print(f"{number1} / {number2} = {divide_numbers(number1, number2)}")

        # Asking user if they want to perform another calculation
        another_calculation = input("Would you like to perform another calculation? (yes/no): ")
        if another_calculation.lower() == "no":
            break
    else:
        print("Invalid option selected. Please choose a valid operation.")
