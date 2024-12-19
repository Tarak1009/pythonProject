class bikes:
    def bike(self,bmw,ducati):
        self.cc1 = bmw
        self.cc2 = ducati
        return self

    def bike2(self, Bimota, beneli):
        self.cc3 = Bimota
        self.cc4 = beneli
        return self

    def __add__(self, other):
        b1= self.cc1 + other.cc3
        b2= self.cc2 + other.cc4
        return b1+b2

    def __gt__(self, other):
        b1= self.cc1 + self.cc2
        b2 = other.cc3 + other.cc4
        if(b1 > b2):
            return True
        else:
            return False

b1 = bikes().bike(1000, 1200)
b2 = bikes().bike2(1300,1066)

b3= bikes.__add__(b1,b2)
print(b3)
b4 = bikes.__gt__(b1,b2)
if (b4 == True):
    print("b1 is greater")
else:
    print("b2 is greater")

# Refer the notes on the OperationOverloading
