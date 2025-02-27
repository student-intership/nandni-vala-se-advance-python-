class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

person1 = Person("Nandni Vala", 21)

print("Accessing properties directly:")
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")

print("\nAccessing properties using a method:")
person1.display_info()
