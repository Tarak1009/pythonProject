# Method Overriding



class A:
    def show(self):
        print("Show A")

class B(A):
    pass

a = B()
a.show()

# 1). Here you can see the class B had no Show method
# 2). Class A which is the super class of class B had the show method so when you called it if executed the show method statement
# 3). Now let me include the show method in the class B

class A:
    def show(self):
        print("Show A")

class B(A):
    def show(self):
        print("Show B")

a = B()
a.show()

# 4). Now you can see the class A Show method is overridden by the class B show method.

