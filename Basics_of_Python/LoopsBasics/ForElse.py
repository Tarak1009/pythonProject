#For Else is specific to python and you don't find in java, c or other languages
# consider the user wants to print the numbers divisible by 5
nums=[10,13,15,81,64]

for num in nums:
    if num%5==0:
        print(num)
    else:
        print(" num divisible by 5 not found")

# What if the user wants to print only first number divisible by 5
nums=[11,13,12,53,64]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
    else:
        print("num divisible by 5 not found")
        # This had printed this statement until the loop gets completed
        # because here the else belongs to if statement

# What if the user wants to print only first number divisible by 5
nums=[11,13,12,53,64]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print(" num divisible by 5 not found")
    # This had printed this statement only once after the loop ended
    # because here the else belongs to for loop