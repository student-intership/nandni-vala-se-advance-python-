global_variable = "I am a global variable"

class ExampleClass:
    def __init__(self, value):
        
        self.local_variable = value

    def demonstrate_variables(self):
        
        local_variable = "I am a local variable"
        
        print(local_variable)  
        print(self.local_variable)  
        print(global_variable)  

example = ExampleClass("I am an instance variable")

example.demonstrate_variables()

print("\nAccessing global variable outside the class:")
print(global_variable)
