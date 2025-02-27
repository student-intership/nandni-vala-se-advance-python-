class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model  
        self.year = year    

    def display_details(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla", 2021)

print("Accessing properties directly:")
print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")

print("\nAccessing properties using a method:")
my_car.display_details()
