# A function which is returnign nothing called 2 times

def add():
    x=5
    y=3
    z=x+y
    print(z)

add()
add()

# A function being called with the Arguments

def add(x, y):
    z=x+y
    print(z)

add(5,4)

# A function being called with arguments returnign the values

def add_sub_mul_div(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d

print(add_sub_mul_div(10,5))

#OR

result1, result2, result3, result4 = add_sub_mul_div(15,3)
print(result1, result2, result3, result4)

