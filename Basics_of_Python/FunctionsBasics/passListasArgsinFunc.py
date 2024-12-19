# print Even and odd numbers from the list that is passed as arguments

def count(lst):
    even=0
    odd=0
    for i in lst:
        if(i % 2 == 0):
            even+=1
        else:
            odd+=1
    return even, odd

lst = [3,5,2,9,6]
even, odd = count(lst)

print("Even: {}, Odd: {}".format(even,odd))

# take list of user and print count and print names who tad names with chars more than 3

def Names(lst1):
    sNames = 0
    bNames = 0

    for i in lst1:
        length = len(i)
        print(length)
        if(length>3):
            bNames+=1
            print(i)
        else:
            sNames+=1
            print(i)
    return sNames, bNames


lst1=["tarak", "Chinnu", "teja", "tarun", "Raja", "Koti", "Lakshmi", "Lakshman", "Tan", "Har"]
sNames, bNames = Names(lst1)
print("Small Names: {}, Big Names: {}".format(sNames,bNames))