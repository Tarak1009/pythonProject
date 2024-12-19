a=10
b=5
try:
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print("Invalid Input: ", e)

except Exception as e:
    print("Some exception occured", e)

finally:            # Finally keyword will execute the block of code written. after the try and Except
    k = int(input("Enter a number"))
    print(k)