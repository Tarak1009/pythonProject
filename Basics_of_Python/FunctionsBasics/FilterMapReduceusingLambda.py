from functools import reduce

def is_even(n):
    return n % 2 == 0
nums = [2,4,5,7,8,9,6]


#we use filter function to filter the values from a list
evenNums=list(filter(is_even,nums))
print(evenNums)

# or

evenNums=list(filter(lambda n : n % 2 == 0,nums))
print(evenNums)

# lets double the values using the map function

double = list(map(lambda n : n * 2, nums))
print(double)

# using reduce function reduce
# reduce is function that belongs to functools
# list is converted to int here because you are adding the values in the list with one another
sum = int(reduce(lambda a,b: a+b,nums))
print(sum)

####### IMP ########
#filter: Selects elements based on a condition.
#map: Transforms elements by applying a function.
#reduce: Aggregates elements into a single value.

