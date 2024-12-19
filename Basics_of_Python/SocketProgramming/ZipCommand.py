names = ("Tarak","Teja","Tarun")
Comps = ("Wipro","Capgemini","Accenture")

zipped = dict(zip(names,Comps))
zipped1 = list(zip(names,Comps))
zipped2 = set(zip(names,Comps))
zipped3 = zip(names,Comps)
print(zipped)
print(zipped1)
print(zipped2)

for (a,b) in zipped3:
    if (a == "Tarak"):
        print(a + "anath")
        print(b)
    else:
        print(a)
        print(b)