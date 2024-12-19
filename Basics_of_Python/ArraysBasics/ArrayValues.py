# create a array with the user inputs
from array import *

arr=array('i',[])           # This step created an empty array

n = int(input("Enter the size of the array"))

for i in range(n):                              # Here the i refers to the range of the array or the size of the array
     K = int(input("Enter the array"))
     arr.append(K)

print(arr)

# Search the array for the value you have entered

searchValue = int(input("Enter the number you want to search for from the array"))
k = 0

for e in arr:                                   #### Here the e refers to the values in the array the values in the array are what gets stored in the e
                                                # you can use this to search or fetch the values in the array
    if e == searchValue:
        print("Match found at index: ",k)
        break
    k+=1
else:
    print("no match found")

########## OR #########

print(arr.index(searchValue))




