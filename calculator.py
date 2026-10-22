def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def calculate(a, operator, b):
    """Perform a calculation based on the selected operator."""
    if operator == "+":
        return add(a, b)

    elif operator == "-":
        return subtract(a, b)

    elif operator == "*":
        return multiply(a, b)

    elif operator == "/":
        return divide(a, b)

    else:
        raise ValueError("Invalid operator.")


if __name__ == "__main__":
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        result = calculate(first_number, operator, second_number)

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)