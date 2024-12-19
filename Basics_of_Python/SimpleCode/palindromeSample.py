from array import array


def pal(input_str):
    list=[]
    p= len(input_str)
    for i in range(p):
        a= input_str[i]
        list.insert(i, a)
    return list

def comp(input_str):
    c=pal(input_str)
    list1= c.copy()                 # Copy method will copy the list to the new list. so it doesn’t assign None to list1.
    list1.reverse()
    print(c)
    print(list1)
    if c == list1:
        print("The string entered is a palindrome")
    else:
        print("The string entered is not a palindrome")


input_str=input("Enter a Palindrome: ")
ip_str= input_str.lower()
comp(ip_str)


