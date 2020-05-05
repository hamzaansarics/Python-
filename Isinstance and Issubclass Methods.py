class Sayen:
    def khan(self,name,age):
        print(name,age)
class Sayen2(Sayen):
    aaa=100
obj=Sayen2()
# obj.khan('hamza ansari',21)

print(isinstance(obj,Sayen))
print(issubclass(Sayen,Sayen2))








