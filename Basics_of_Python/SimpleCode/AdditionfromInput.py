
x=int (input("Enter 1st number"))       #by default the values are considered as string when we use input method
y=int (input("Enter 2nd number"))

z=x+y
print(z)

#use indexing to print a specific char from a string
char=input("Enter a character")
print(char[0])                          # after fetching it is fetching the 0th index

#or

char=input("Enter a character")[0]      #while reading itself it will read the 0th index
print(char)

#Eval will evaluate the text and give us the result
x=eval(input("Enter your expression"))
print(x)


#this way you can pass the values from the command prompt while starting to execute the code 
# C:\Users\ANNE TARAKANATH\PythonLearner\pythonProject>python AdditionfromInput.py 5 6
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
z=a+b
print(z)
