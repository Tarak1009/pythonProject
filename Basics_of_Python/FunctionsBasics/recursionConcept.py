import sys

print(sys.getrecursionlimit())                  # usually in python the recursion limit is 1000
sys.setrecursionlimit(2000)                     # But you can customize and increase the limit too

i=0
def great():
    global i
    i += 1
    print("Hello", i)
    great()

great()