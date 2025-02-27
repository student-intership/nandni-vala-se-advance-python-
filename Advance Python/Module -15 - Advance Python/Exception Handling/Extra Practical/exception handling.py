def exceptions():
    try:
        filename = input("Enter the filename to open: ")
        with open(filename, 'r') as file:
            print("File content:")
            print(file.read())

        n = int(input("Enter number : "))
        n1 = int(input("Enter number 1: "))
        result = n / n1
        print(f"The result of division is: {result}")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values where required.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print("Operation completed successfully!")

    finally:
        print("Program execution finished.")



exceptions()
