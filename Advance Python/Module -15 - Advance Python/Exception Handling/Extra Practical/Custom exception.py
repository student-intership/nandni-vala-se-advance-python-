class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
def check_value(value):
    try:
        if value < 0:
            raise CustomException("Negative values are not allowed.")
        elif value == 0:
            raise CustomException("Zero is not a valid input.")
        else:
            print(f"Valid value: {value}")
    except CustomException as e:
        print(f"Custom Exception: {e.message}")

try:
    user_input = int(input("Enter a value: "))
    check_value(user_input)
except ValueError:
    print("Invalid input. Please enter a numeric value.")