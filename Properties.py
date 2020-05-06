class Pa:
    @property
    def id(self):
        return self.id1
    @id.setter
    def id(self,ID):
        self.id1=ID

oo=Pa()
oo.id=90
print(oo.id)












