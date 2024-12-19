# Compile Time Error:
# Compile time error are errors that occur while compiling the code
# Eg: Syntax errors
# Most easy to handle
from logging import exception

# Logical Error:
# Logical Errors are errors that occurs due to the wrong input or wrong logic. these error will not be compile time error or run time error.
# Eg: 2+3 = 5 but if you get 2+3 = 4 then this is a logical error because there is something wrong with the logic
# logical errors can be corrected because we have testers testing the application.

# Run Time Error:
# Run time errors are errors that occur while executing the code. will be compiled perfectly. it will have a problems with only few inputs like
# Eg: Divide by 0

# If there is No error you can also execute all the steps
a=5
b=2

print(a/b)
print("Bye")

# If there is a error and if you want to execute all the steps in this example print("Hey") then we need to use the Try except method.
a=5
b=0
try:
    print(a/b)
# In this example, e holds the ValueError instance, and it can provide a message or other information about what went wrong.
# You can choose any variable name for the exception object, but e is commonly used by convention.
except Exception as e:
    print("Hey you can't enter a zero: ", e)

print("Hey")

# Best coding practice.....
# When ever you open a resource (A Resource can be a file, DB connection you tried opening)  you must clode it and do not forget.
# here is the example of it

a=5
b=0

try:
    print("Resource Opened")
    print(a/b)
except:
    print("Hey you can't enter a zero: ")

# Finally keyword will execute if we get an error as well as if we don't get an error.
finally:
    print("Resource Closed")