# class Pak:
#     __eid=100
#     def setid(self,id):
#         self.__eid=id
#     def disid(self):
#         print(self.__eid)
# os=Pak()
# os.disid()
# os.setid(200)
# os.disid()
class khan:
   def __securedata(self):
       print("This is Not a Private Function but they are become Private")
   def showsecurefunction(self):
       self.__securedata()
obj=khan()
obj.showsecurefunction()
obj.__securedata()











