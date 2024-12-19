class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Mycharm:
    def execute(self):
        print("Spell Check")
        print("Conventional Checks")
        print("Compiling")
        print("Running")

class Run:
    def code(self, ide):
        ide.execute()


#ide=pycharm()
p=Mycharm()

r= Run()
r.code(p)

# Duck Typing: The class Run is expecting an argument and expecting execute method from the class to which the object is referring to.
# So when the object refers to a class which had execute method in it then it will work.

# Duck typing will not be concerned about the class to which the object is referring to until it had the execute method in it.
# In this case Pycharm and Mycharm are 2 classes which had Execute method
# r.code(p) will work with both Mycharm and Pycharm because it had execute method

