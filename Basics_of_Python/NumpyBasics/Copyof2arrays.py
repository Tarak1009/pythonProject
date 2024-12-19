from numpy import *
# Both the arrays are using the same the address
arr1 = array([4, 5, 6, 7])
arr2 = arr1

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

# Shallow Copy
# Both the arrays are using the different addresses but the shallow copy happened....
# so changing the value in the 1st array is changing the value in the 2nd array
arr1 = array([4, 0, 6, 7])
arr2 = arr1.view()
arr1[1]=12

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

# Deep Copy
# Both the arrays are using the different addresses with the deep copy happened....
# so changing the value in the 1st array is not going to change the value in the 2nd array
arr1 = array([4, 7, 3, 7])
arr2 = arr1.copy()
arr1[3]=4
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

