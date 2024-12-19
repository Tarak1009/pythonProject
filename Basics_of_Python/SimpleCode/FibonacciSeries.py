#Fibanocci series
def fib(userNum):
    a = 0
    b = 1
    if(userNum < a):                              #write a code to not accept the negative numbers
        print("Enter Positive number")
    else:
        if(userNum < 1):
            print(a)
        else:
            print(a)
            print(b)

            for i in range(2, userNum):         #You started from 2 because the first 2 numbers are already printed in a fibonacci number
                c=a+b
                a=b
                b=c
                if (c <= SeqNum):              # here you are checking if the generated fibonacci number is less than the given number
                                                # and only printing the if it is less than it
                    print(c)
                    if (b == SeqNum):
                        print("The number" ' ', SeqNum, ' ' "is in the series")
                    else:
                        print("The number" ' ', SeqNum, ' ' "is not in the series")
                else:
                    break


userNum=int(input("Enter your Number"))
SeqNum= int(input("Enter your Number to check if it fibonacci"))
fib(userNum)