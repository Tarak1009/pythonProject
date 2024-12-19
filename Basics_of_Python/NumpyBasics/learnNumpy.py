from os import cpu_count

from numpy import *

lins = linspace(1, 2, 4)
print(lins)
# ins linspace 1 is start 2 is stop and 4 is number of parts you want to divide these numbers into in between the numbers provided
# linspace will always have values in float because in divisions you might end up with decimals

logs = logspace(1, 2, 4)
print(logs)
# logspace is same as linspace but the only difference is in linspace we will take the regular intervals...
# but in log space we will take the log base 10 of the random intervals between the start and stop numbers start and stop numbers will the same

aran = arange(3, 18, 2)
print(aran)
#arange is same as range it will print the values by skipping the 2 steps if we take above scenario

zer = zeros(5)
print(zer)

one = ones(6)
print(one)

arr1 = array([6,7,1,9])
arr2 = array([1,7,9,3])
arr3 = arr1+arr2                # vector addition:- Addition of 2 arrays
print(arr3)

print(arr1*2)


print(log(arr3))
print(sin(arr3))
print(cos(arr3))
print(sqrt(arr3))

print(sum(arr1))
print(max(arr1))

#concatenate 2 arrays
print(concatenate([arr1,arr2]))
