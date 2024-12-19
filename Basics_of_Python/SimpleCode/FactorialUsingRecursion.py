
def fact(n):
    if(n == 0):
        return 1
    return n * fact(n-1)

num = int(input("Enter a Number"))
result = fact(num)
print(result)

#Think of it like a stack of boxes:

#   1. When you call fact(5), you place the 5 box on top.
#   2. It needs to know what fact(4) is, so it puts a 4 box on the stack.
#   3. This continues down to the 0 box.
#   4. Once it reaches the base case and returns 1, it starts removing boxes from the stack and calculating:


