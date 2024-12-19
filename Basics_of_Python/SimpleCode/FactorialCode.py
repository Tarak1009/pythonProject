
# Simple factorial code
def fact(num):
    for i in range(1, num):
        num = num * i
    return  num



num = int(input("Enter a number"))
result = fact(num)
print(result)


#num = num*(num-1)*(num-2)
# Factorial using Recursive