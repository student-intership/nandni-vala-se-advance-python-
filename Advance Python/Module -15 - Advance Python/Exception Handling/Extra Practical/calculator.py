def calculator():
    try:
        # Prompt user for inputs
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        operation = input("Enter the operation (+, -, *, /): ").strip()

        # Convert inputs to numbers
        num1 = float(num1)
        num2 = float(num2)

        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2  # Division by zero will raise an exception
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
            return  # Exit the function

        print(f"The result is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    
    
calculator()


