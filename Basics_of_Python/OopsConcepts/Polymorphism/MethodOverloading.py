
# Method Overloading:
# The same method name can be called with different arguments, and passing different arguments calls another method based on the arguments that match.
# Python doesn't support method over loading but, you can achieve it in following way
class A:

    def __add__(self, a=None, b=None, c=None):
        d=0
        if a != None and b != None and c != None:
            d=a+b+c
            return d
        elif a != None and b != None:
            d=a+b
            return d
        elif a != None:
            d = a
            return d


a = A()
r= a.__add__(5)
print(r)
