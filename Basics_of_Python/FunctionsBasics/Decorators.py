# Decorators: Decorators are functions that performs a certain operation of the other function which shouldn't be changed altering the unchangeble functions results


# Function that shouldn't be changed
def div(a,b):
    print(a/b)



#here let's suppose you want to print the value as 4/2 even when we recieved as 2/4
#normally what we do is....
# but this a unchangeable function so we can use like this so use a decorator

#def div(a,b):
#    if a<b:
#        a,b = b,a
#    print(a/b)
# When we use decorators, we want to wrap the original function so that it gains some additional behavior but can still be called like the original function.

def interchange(func):

    def inner(firstNum,seconNum):
        if firstNum<seconNum:
          firstNum,seconNum = seconNum,firstNum
        return func(firstNum,seconNum)

    return inner

a = int(input("1st Num"))
b = int(input("2nd Num"))
div1 = interchange(div)
div1(a,b)