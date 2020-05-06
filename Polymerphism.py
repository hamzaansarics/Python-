class Phone:
    def __init__(self,brand,modal):
        self.brand=brand
        self.modal=modal
    def modata(self):
        return f'{self.brand},{self.modal}'
class vivo(Phone):
    def __init__(self,brand,modal,pice):
        super().__init__(brand,modal)
        self.pice=pice
    def modata(self):
        return self.brand,self.modal,self.pice
ok=vivo('Nokia',1200,120000)
aa=Phone('Nokia',19200)
print(aa.modata())
print(ok.modata())





