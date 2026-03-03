"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""
def sanitize_input_request(input_val: str, operation: bool) -> float | str:
    """Function to request a number/operation input: if the input is not a number/operation it will keep asking until it gets one"""
    if not operation:
        try:
            input_f = float(input_val)
            return input_f
        except ValueError:
            return sanitize_input_request(input("That's not a number! Try again: "), False)
    else:
        if input_val.strip().lower() in ['add', 'subtract', 'multiply', 'divide']:
            return input_val.strip().lower()
        else:
            return sanitize_input_request(input("That's not a valid operation! Try again: "), True)

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = sanitize_input_request(input("Enter the first number: "), False)
    num2 = sanitize_input_request(input("Enter the second number: "), False)
    operation = sanitize_input_request(input("Enter the operation: "), True)

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
