class A:
    def laptop1(self):
        print("you have a HP laptop")

    def laptop2(self):
        print("you have a Lenovo laptop")

class B(A):             # Single Inheritance
    def laptop3(self):
        print("you have a Sony laptop")

    def laptop4(self):
        print("you have a Dell laptop")

class C(B):             # Multi level inheritance
    def book1(self):
        print("Compound Effect")

    def book2(self):
        print("You Can Win")

class D:
    def book3(self):
        print("How to win friends and influence people")

    def book4(self):
        print("Subtle Art of Not giving a fuck")

class E(A,D):       #Multiple Inheritance
    def book5(self):
        print("The Monk who sold his ferrari")

    def book6(self):
        print("The 5 AM Club")


l1= A()
l1.laptop1()

l3=B()
l3.laptop3()


e1 = E()
e1.laptop2()