import array


import array as a
#from array import *



# 1st this will import array and the object we use to call methods in this class is array
# 2nd this will import array and the object we use to call methods in this class is a because i have given the alias as a
# 3rd this way you can only call the method you want to import from the array class .....
# here I have put * ( regukar Expression indicating that I will use every method in the class

val = array.array('i',[5,3,-4,8,10])        #i unsigned integer
print(val)

# instead
val = a.array('I',[5,3,4,8,10])             #I signed integer
print(val)

val= array.array('f',[7.3,4.8,9,10])        #f float
print(val.buffer_info())

val= array.array('d',[7.3,4.8,9,10])        #d double float
print(val.buffer_info())

#Print the values of array one by one

val= array.array('u',['c','t','b','y'])          #u unicodechar
count=len(val)
for i in range (count):
    print(val[i])



#or

vals= a.array('i',[1,2,4,7])       #Getting error let me see later
for i in vals:
    print(vals[i])

val = array.array('i',[5,3,-4,8,10])        #i unsigned integer

newArr= array.array(val.typecode,(array*2 for array in val))        # creating the new array(newArr) from the old array val
print(newArr)

for e in newArr:
    print(e)
