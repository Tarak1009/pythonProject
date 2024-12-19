# Linear Search: Linear search is the
list=[5,9,20,28,21,40]
n=int(input("Enter a number to search: "))
pos = 0
def search(l,n):
    i = 0
    while i< len(l):
        if list[i] == n:
            return True
        i = i + 1
        globals()['pos'] = i

    else:
        return False


if search(list,n):
    print("Found it at: ", pos)

else:
    print("Not Found")