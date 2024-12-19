####     selection sort         ####


list=[1,4,2,100,72,56,38,29,3,18]
c = len(list)
def sortAsc():
    for i in range(c):
        min=i
        for j in range(i+1,c):
            if(list[j] < list[min]):
                min = j
        list[i],list[min] = list[min], list[i]
        print(list)
    return list


list1=[1,4,2,100,72,56,38,29,18,3]
c1=len(list1)
def sortDesc():
    for k in range(c1):
        min1 = k
        for l in range(k + 1, c1):
            if (list[l] > list[min1]):
                min1 = l
        list[k], list[min1] = list[min1], list[k]
    return list
print(sortAsc())
print(sortDesc())