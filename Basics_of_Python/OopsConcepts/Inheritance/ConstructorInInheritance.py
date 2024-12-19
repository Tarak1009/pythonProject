
class A:

    def __init__(self):
        print("Looper")

    def Superman(self):
        print("Man of Steel")

class B(A):
    def __init__(self):
        print("Tenet")

    def Batman(self):
        print("The Dark Knight")

class C(B):
    def __init__(self):
        super().__init__()
        print("Interstellar")

class D:
    def __init__(self):
        print("Init Flash D")

    def SpiderMan(self):
        print("Spider-Man")

        def Flash(self):
            print("Flash D")

class E:
    def __init__(self):
        print("Init Flash E")

    def IronMan(self):
        print("Ironman")

    def Flash(self):
        print("Flash E")

class F(D,E):

    def __init__(self):
        super().__init__()
        print("Init Flash F")
    def Flash(self):
        super().Flash()
        print("Flash F")

c1 = C()
f1 = F()

### Look at the description written in the notes


