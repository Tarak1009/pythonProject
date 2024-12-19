# Abstract Method:
# The method the has a declaration but no definition is called as Abstract Method
# Abstract Class:
# The Classes which has Abstract Methods is called as Abstract Class

# Abstract classes cannot be called or instanciated using an object

# Python by default do not support the Abstract class and Abstract method

from abc import ABC, abstractmethod

class tasks(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Vehicle(tasks):
    def start(self):
        print("The Vehicle started")
    def stop(self):
        print("The Vehicle stopped")



v = Vehicle()
v.start()
v.stop()