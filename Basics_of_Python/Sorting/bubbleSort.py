list=[5,3,6,8,7,9,2,10,87,100,92,1]
# Ascending order
def sortAsc():
    for j in range(len(list)):
        for i in range(len(list)):
            if i+1 == len(list):
                    break
            elif list[i] > list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]

    return list

list1=[5,3,6,8,7,9,2,10,87,100,92,1]

# Descending Order

def sortDesc():
    count = len(list) - 1
    for l in range(count):
        for k in range(count,0,-1):
            if k-1 == count:
                break
            elif list1[k] > list1[k - 1]:
                list1[k], list1[k - 1] = list1[k - 1], list1[k]
    return list1


print(sortAsc())
print(sortDesc())