class Pai:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Meu nome é: " +self.nome
class Filho(Pai):
    def __init__(self, nome):
        Pai.__init__(self, nome)

obj1 = Pai("Chicolomuenho")
print(obj1)
obj = Filho("Antunes")
print(obj)