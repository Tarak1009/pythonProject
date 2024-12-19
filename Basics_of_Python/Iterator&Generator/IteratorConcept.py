#Iterator: We use Iterator to fetch the values one by one from the List

#nums=[3,5,6,9]

#it= iter(nums)
#print(it.__next__())
#print(it.__next__())

###### OR #######
#print(next(it))
#print(next(it))

##how can we use iterator to do our own stuff
class topten:
    def __init__(self):
        self.nums= 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nums <= 10:
            val= self.nums
            self.nums +=1
            return val
        else:
            raise StopIteration

values= topten()
print(values.__next__())

## Good point to remember for both Iterator and Generator is when you try to fetch the value using the next method and if the loop starts running in the below line
# then it will run from the succeeding value
# Because it will pick from the 2 not from 1 again

for i in values:
    print(i)