import SpecialCharacter
# name is a Special variable
# __name__ indicates that this is the main program and the execution should start from here
# Like main function in java

# Name value changes as per the place you are using it
#in the Special Character you have written the __name__ and you have imported the SpecialCharacter module
# So the __name__ will print the name of the module in this case it is SpecialCharacter

# What if you have imported the DemoSpecialCharacterto the SpecialCharacter module
# Then it will print the DemoSpecialCharacter as it is the imported module


print(__name__)
