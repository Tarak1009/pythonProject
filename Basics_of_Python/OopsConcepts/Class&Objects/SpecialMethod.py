class computer:
# __init__ is a special method it is a constructor
    # When you access self.CPU, Python knows you’re referring to the CPU attribute of the current instance (self).
    # Without self, CPU and RAM would be treated as local variables, and since they’re not defined locally within Config, Python would throw an error.
    # Parameterized Constructor is constructor with parameters.
    # The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
    def __init__(self,CPU,RAM):
        self.C = CPU
        self.R = RAM

    # When you call c1.Config(), Python:

    # 1. Python Knows self refers to c1.
    # 2. Looks up self.CPU and self.RAM on c1, retrieving the values you set earlier in __init__.

    def Config(self):
        print("Your PC Details: " ,self.C, self.R)
    # Why You Need self in the print Statement
    # 1. Without self, the print statement wouldn’t know where to look for CPU and RAM, because there’s no local definition within Config.
    # 2. Using self tells Python, “look for these values in the instance that called this method.”


c1 = computer("i5", "32GB")
c2 = computer("Ryzen7", "64GB")

c1.Config()
c2.Config()

