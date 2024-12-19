# usually you right it this way

def mul(a):
    a= a*a
    return a

result= mul(5)
print(result)

# Anonymous functions

mul=lambda  a : a*a         # in Python Functions are also objects
# Anonymous functions use lamba keyword to represnt them
# mul in the above step is the object of that anonymous function
# you call the function using the object of that function like we did here
# Anonymous functions should only have one expression in this case .... it is a*a


result= mul(5)
print(result)

# Anonymous function2
f= lambda a,b: a+b

print(f(5,6))