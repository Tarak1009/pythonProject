

def simplePrint():
    print("Hello "  +  __name__)
    print('Welcome back')


if __name__ == "__main__":
    simplePrint()

# Here if you run this code from the SpecialCharacter moduel you will be able to print heloo and welcome back because __name__ = __main__ ...
# ...because you are in the same module

# but if you try to run the code from the DemoSpecialCharacter which had this SpecialCharacter module imported you can't run it...
# ... because the __name__ is SpecialCharacter now

