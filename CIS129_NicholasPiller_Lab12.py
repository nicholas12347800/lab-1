class Pet:
    def __init__(self, name="", type_="", age=0):
        self.name = name
        self.type = type_
        self.age = age
    
    # Setters (mutators)
    def setName(self, name):
        self.name = name
    
    def setType(self, type_):
        self.type = type_
    
    def setAge(self, age):
        self.age = age
    
    # Getters (accessors)
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getAge(self):
        return self.age

def main():
    # Create a Pet object
    animal = Pet()
    
    # Set the pet's information directly (as requested)
    animal.setName("Sophie")
    animal.setType("Dog")
    animal.setAge(8)
    
    # Display the pet's information
    print(f"\nThe pet name is {animal.getName()}")
    print(f"The pet type is {animal.getType()}")
    print(f"The pet age is {animal.getAge()}")

if __name__ == "__main__":
    main()
