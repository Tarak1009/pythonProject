list=['tarak',10,9.6]
print(list)
list.reverse()
print(list)
list.append(2)
list.pop(1)                         #index
list.remove('tarak')

print(list)

print('\n')

tuple=('tarak',10,14.6)
print(tuple)
print(tuple[0])
print('\n')


set1={1,5,9,7,7,8,7}
set2={6,10,5,1,13}
set2.add(7)
set3=set1.union(set2)
set4=set1.intersection(set2)
print(set3)
print(set4)

dic={"tarak":"Pizza", "chinnu":"Pasta", "teja":{"Biryani", "Momos"}, "Bava":("Chicken","Mutton"), "Amma":["soup",1/2 ,"chilli Paneer"]}
print(dic)
print(dic["tarak"])
print(dic["teja"])                          #print(dic["teja"][0]) this will not work because the set is not storing the values based on the index
print(dic["Bava"][0])
print(dic["Amma"][1])

