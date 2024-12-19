from numpy import *

arr= array([1,7,9,10])          # normally and array is 1 dimensional with 1 row  and multiple columns
print(arr.shape)

# using the below syntax you can make the array any dimensional with any no. of rows and columns
arr1 = array ([
        [1,2,3,4],
        [5,6,7,8]
        ])
print(arr1)

print(arr1.dtype)               # datatype of the array
print(arr1.size)                # Size of the array combining the dimensions in the arrays in the
print(arr1.ndim)                # no. of dimensions in the array
print(arr1.shape)               # shape will give you the rows and columns of the array

arr2=arr1.flatten()             # flatten flattens the dimensions and converts to single dimensional array
print(arr2)


#print(arr2.reshape(4,2))
#arr3 = (arr2.reshape(2,2,3))

m = matrix(arr1)
print(m)

m1=matrix('1 2; 3 4')
print(m1)

m2=matrix('2 3; 4 5')
print(m2)

m3 = m1 + m2
print(m3)
m3 = m1 * m2
print(m3)




