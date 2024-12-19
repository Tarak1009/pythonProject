class bikes:
    # Class Variable or Static Variable
    wheels=2            # stored in the Class Namespace
    def __init__(self):
        # Instance Variable
        self.mil = 30               # stored in the Instance Namespace
        self.brand = "RE"

c1=bikes()
c2=bikes()
c2.wheels = 4
bikes.wheels=3
print(c1.mil, c1.brand, c1.wheels)
print(c2.mil, c2.brand, bikes.wheels, c2.wheels)

