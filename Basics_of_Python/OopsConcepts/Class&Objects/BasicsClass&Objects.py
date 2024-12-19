class computer:
# Class computer had one method
    def demo1(self):
        print("Windows, 16gb, 1TB")

# Assigning the object d1 and d2 to the class computer
d1 = computer()
d2 = computer()

# Demo method belongs to class computer and we have to pass the object
computer.demo1(d1)
computer.demo1(d2)

# Here d1.demo1() is calling the method d1 of the class to which it is instantaneoused
d1.demo1()
d2.demo1()

