def demonstrate_exceptions():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"The result of division is: {result}")
        
        my_list = [10, 20, 30,'Hello',1.20]
        index = int(input("Enter the index to access from the list: "))
        print(f"The value at index {index} is: {my_list[index]}")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    
    except IndexError as ie:
        print(f"Error: {ie}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

demonstrate_exceptions()

