# Unchangeable code
def Sub(a,b):
    c=a - b
    print(c)


# Initiate a Decorator
def interchage(func):

    def actInterchange(a,b):
        if(a < b):
            a,b = b,a
        return func(a,b)

    return actInterchange

x=int(input("1st Num"))
y=int(input("2nd Num"))
Sub1=interchage(Sub)
Sub1(x,y)