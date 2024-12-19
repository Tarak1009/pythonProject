#Position Argument

# Position arguments: the arguments we pass take the position by default
def person(name,age):
    print(name)
    print(age-5)

person("tarak",29)

#person(29,"tarak")          # this will fail because age is accepting the string and string cannot be subtracted...
                                       # instead we can use keyword arguments
# Keyword Argument
person(age=29, name="tarak")

# Default Argument
def person2(name,age=18):        # this is an example of default argument here you specified the age is 18 in the declaration of the function itslef
    print(name)
    print(age)

person2("tarun")                        # you can call using the single argument because the age is already defined or..

person2("tarun",29)         # you can call with the age and it will replace the existing value 18 and it will use the new value defined in the calling function

# Variable length argument
# here you have a scenario where you have a function accepting 2 arguments but in the calling function you want to pass multiple arguments
#def sum(a,b):
#    c=a+b
#    print(c)
#sum(9,10,2,1)

# this code will fail because you can see a=9 b= 10, 2, 1 are left

# here is the corrected version using the variable length concept...
# where you have made the last argument as tuple using *b

def sum(a, *b):
    c = a
    for i in b:
        c = c+i
    print(c)

sum(9,10,2,1)

#or

def sum(*b):
    c = 0
    for i in b:
        c = c+i
    print(c)

sum(9,10,2,1)

# Keyword Variable length arguments
def personData(name, **b):
    print(name)
    for i,j in b.items():
        print(i,j)

personData("tarak", City="Vijayawada", HouseN0=2, Street="Ram nagar")

