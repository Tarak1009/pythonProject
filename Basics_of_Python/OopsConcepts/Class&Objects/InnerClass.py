class student:

    def __init__(self, name, age, rollNo):
        self.n = name
        self.a = age
        self.r = rollNo
        self.lap = self.laptop()                # you are calling the inner class in the outer class both will work

    def show(self):
        print("Name: ",self.n, "Age: ", self.a, "Roll No: ", self.r)

    class laptop():

        def __init__(self):
            self.comp = "HP"
            self.Ram = "16GB"
            self.CPU = "Ryzen 7"
            self.Memory = "1TB"

        def show(self):
            print(self.comp, self.Ram, self.CPU, self.Memory)

s1=student("Tarak", 21, 55)
s2=student("Chinnu", 19, 16)

s1.show()
s2.show()

s1.lap.show()                       # if the inner class is defined in the outer class you need to call it with the abject using the outer class and then use the inner class

l1=student.laptop()                 # you are calling the inner outside the outter class but first you need to call it with the help of the outer
l1.show()
