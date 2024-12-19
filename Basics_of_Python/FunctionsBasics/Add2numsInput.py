#Add 2 numbers with the input from the user  using the concept of functions

def add2nums():
    FirstNum=int(input("Enter the First number"))
    SecondNum=int(input("Enter the Second number"))

    sum=FirstNum+SecondNum
    sub=FirstNum-SecondNum
    mul=FirstNum*SecondNum
    div=FirstNum/SecondNum

    return sum, sub,mul,div

r1, r2, r3, r4=add2nums()
print(r1, r2, r3, r4)