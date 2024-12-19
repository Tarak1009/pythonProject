# Generator: generator will give you iterator
# yield will return the value in the form of iterator. so you need to use __next__()

def Gen():
    yield 1
    yield 2
    yield 3
    yield 4

g=Gen()
print(g.__next__())

def num():
    num=1
    while num <= 10:
        v=num*num
        yield v
        num+=1

n=num()
print(n.__next__())

## Good point to remember for both Iterator and Generator is when you try to fetch the value using the next method and if the loop starts running in the below line
# then it will run from the succeeding value
# Because it will pick from the 2 not from 1 again

for i in n:
    print(i)