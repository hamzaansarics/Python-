class khan:
    def __init__(self,brand,modal):
        self.brand=brand
        self.modal=modal
    def __str__(self):
        return f'{len(self.brand)}'
obj=khan('Nokia',1112)
print(obj)


