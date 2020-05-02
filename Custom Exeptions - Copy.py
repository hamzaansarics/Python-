class ShortLength(ValueError):
    pass

class khan:
    def show(self,name):
        if len(name)<6:
            raise ShortLength("Lentgh is Very Short")
        else:
            return name
o=khan()
print(o.show('khan'))

