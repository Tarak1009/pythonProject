# Write a peice of code to check if the given number is prime number or not
Number=int(input("Enter a number"))
for i in range (2,Number,1):
    if Number % i == 0:
        print("It is not a prime number")
        break
else:
    print("The number you have entered is a prime number")