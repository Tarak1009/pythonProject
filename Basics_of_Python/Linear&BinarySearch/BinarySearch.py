n = int(input("Enter a number: "))
list = [10,14,15,18,19,20,22,31,45,62,70,71,82,90,91,93]
pos = 0
def search(list,n):
    i = 0
    l = 0
    u = len(list)
    mid = (l+u) // 2
    while l <= u:
        mid = (l + u) // 2
        try:
            if list[mid] == n:
                globals()['pos'] = mid
                return True
            else:
                if list[mid] < n:
                    l = mid+1
                    print(l)
                else:
                    u = mid-1
                    print(u)
        except IndexError as e:
            print(e)
            break
    return False

if search(list,n):
    print("Found", n, "at: ", pos)

else:
    print("Not Found")