class students:

    School = "Nirmala"              # Class variable

    def __init__(self,marks1, marks2, marks3):
        self.m1 = marks1
        self.m2 = marks2
        self.m3 = marks3

    # Instance Method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3          # instance method will use self keyword

    def get_m1(self):               # Accessor Method: This will get the value
        return self.m1

    def set_m1(self):               # Mutator Method: This will set(change) the value
        self.m1 = 51

    @classmethod                    # Decorator
    def schoolName(cls):            # Class Method will use cls keyword
        return cls.School

    @staticmethod                   # Decorator
    def info():                     # Static method will not have any keyword
        print("Static Class")

s1= students(35,12,53)
s2= students(82, 67,71)


print(s1.avg())
print(s2.avg())

print(students.schoolName())
students.info()