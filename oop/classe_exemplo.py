class Exemplo:
    def __init__(self, val=1):
        self.primeiro = val

    def setSegundo(self, val):
        self.segundo = val

o1 = Exemplo()
o2 = Exemplo(2)

o2.setSegundo(3)

o3 = Exemplo(4)
o3.terceiro = 5

print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
