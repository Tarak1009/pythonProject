class Computer:
    # Default Constructor.....
    # Default Constructor The default constructor is a simple constructor which doesn’t accept any arguments.
    # Its definition has only one argument which is a reference to the instance being constructed(self).
    def __init__(self):           # Self is the current instance of the object
        self.name = "Tarak"
        self.age = 21                # Pass will pass the steps inside the class

    def update(self):
        self.age = 12


    def compare(self,obj):
        if(self.age == obj.age):
            return True
        else:
            return False


c1=Computer()
c2=Computer()

c2.update()                        # you have 2 objects created for the class computer so to call the methods in the same class you can use the objects defined previously

if (c1.compare(c2)):
    print("age is same")
else:
    print("age is different")
# Everytime a new object is created it will create a new memory in the heap memory
# And the size of the memory depends on the no.of varaibles and size of each variable
# Who allocates the size to the memory?         ... It is constructor
print(c1.name)                      # self keyword will identify the c1 as the object for this call
print(c2.name)
print(c1.age)
print(c2.age)
print()

