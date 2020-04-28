from abc import ABC,abstractmethod
class Abstract(ABC):
    @abstractmethod
    def area(self):
        pass
class Khan(Abstract):
    def area(self):
         print("This is Khan Method for Abstract Method")
obj=Khan()
obj.area()



