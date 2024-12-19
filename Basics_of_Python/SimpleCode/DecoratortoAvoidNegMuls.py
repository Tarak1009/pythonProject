# Decorator to avoid the negative multiplications

def muls(a, b):
        c= a*b
        print(c)

def convertToPositive(func):

    def inner(a, b):
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        return func(a, b)

    return inner

a=int(input("Enter 1st num"))
b=int(input("Enter 2nd num"))
muls1= convertToPositive(muls)
muls1(a,b)


