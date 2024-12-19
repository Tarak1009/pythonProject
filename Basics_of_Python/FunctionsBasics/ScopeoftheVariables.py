#Scope of the variables
a=10                        # Global Varialbe

def fun1():
    a=15                    # Local Variable
    print("inside",a)

fun1()

print("outside",a)

# Accessing the global variable outside the function

a=9

def fun2():
    global a                # Global keyword will call the variable 'a' that is outside of the fun2()
    print("in",a)

fun2()

print("out",a)

#Changing the global variable from inside the function to affect the global variable
a=14
print(id(a))
def fun3():
    a = 55                      # even when we have variable 'a' here, we will not use it because we are referring the global variable a in the below step.
    x = globals()['a']          # The Global keyword will return all the global varibles so specify the one you want to use
    print(id(x))                # the local variable and global variable are both having the same address
    print("in",x)
    globals()['a'] = 15         # if you want to change the global variable a from the function you can do this like this

fun3()

print("out",a)

