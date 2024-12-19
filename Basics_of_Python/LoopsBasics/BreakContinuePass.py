#you have 10 pens and someone comes to buy pens
#example for Break; break will end the loop
av=5

i=1
x=int(input("Enter no.of pens you want to buy"))

while i<=x:

    if i>av:
        print("out of stock")
        break;
    print('pen', i)
    i+=1

#Example for continue and pass

#continue will continue the execution even when the condition fails by moving to the next iteration
#pass statement simply does nothing. We use pass statement to write empty loops



for i in range(1, 10):
    if i%5!=0:
        print('is not divisible by 5')
        continue;
    print(i)

for i in range(1, 10):
    if i%5==0:
        continue;
    print(i)

for i in range(1, 10):
    if i%5==0:
        pass;
    print(i)