class namesFav:

    def __init__(self):
        self.breed = "Lab"
        self.breed2 = "golden Retriever"

    def person(self):
        self.p1 = "Tarak"
        self.p2 = "Chinnu"

    def printState(self):
        print("These are people and dogs: " , self.breed,self.breed2,self.p1,self.p2)

c1= namesFav()
c2= namesFav()
c1.person()
c2.person()
print(c1.printState())

print(c1.p1)
print(c1.p2)
c1.p1 = "Tarun"
print(c1.p1)
c2.p2= "Teja"
print(c2.p2)

print(c1.breed)
print(c1.breed2)
print(c2.breed)
print(c2.breed2)


