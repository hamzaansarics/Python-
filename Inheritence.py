# class Pa:
#     @property
#     def id(self):
#         return self.id1
#     @id.setter
#     def id(self,ID):
#         self.id1=ID
# class Ch(Pa):
#     @property
#     def name(self):
#         return self.name1
#     @name.setter
#     def name(self,Name):
#         self.name1=max(Name,0)
# oo=Ch()
# oo.id=90
# oo.name=100
# print(oo.name,oo.id)
# ///////////// Multilevel Inheritence /////////////
# class Parent:
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
# class Child1(Parent):
#     def __init__(self,Name,Age,Adress):
#         super().__init__(Name,Age)
#         self.Adress=Adress
#
# class Child2(Child1):
#     def __init__(self,Name,Age,Adress,id):
#         super().__init__(Name,Age,Adress)
#         self.id=id
#     def ALLPP(self):
#         return self.Name,self.Age,self.Adress,self.id
# oj=Child2('Hamza Ansai',21,'Kalowal Pakisan',101)
# print(oj.ALLPP())
# print(help(Child2))

#///////// Multiple Inheritence ///////////
# class Pa:
#     kha=''
# class Ch1:
#     ae=0
# class Ch3:
#     lksdj='jskldjkl'
# class Ch2(Pa,Ch1,Ch3):
#     y=0
#     def show(self):
#         return self.ae,self.y,self.kha,self.lksdj
# kaoo=Ch2()
# kaoo.kha='Kalowal Pakisaan'
# kaoo.ae=90
# kaoo.y=101
# print(kaoo.show())
# print(help(Ch2))









