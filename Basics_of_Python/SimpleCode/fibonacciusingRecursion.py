def fibo(num, a=0, b=1, count=0):
    if(count < num):
        c = a + b
        print(c)
        return fibo(num, b, c, count+1)



n = int(input("Enter your Number: "))
fibo(n)


