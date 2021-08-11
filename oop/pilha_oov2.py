class Pilha:
    def __init__(self):
        self.__minha_pilha = []

    def inserir(self, item):
        self.__minha_pilha.append(item)
        print("Estado da pilha: ", self.__minha_pilha)

    def remover(self):
        item = self.__minha_pilha[-1]
        del self.__minha_pilha[-1]
        #print("Elemento removido: ", item + "\nEstado da pilha: ", self.__minha_pilha)
        return item

class AdicionandoPilha(Pilha):
    def __init__(self):
        Pilha.__init__(self)
        self.__soma=0

    def inserir(self, item):
        self.__soma +=item
        Pilha.inserir(self, item)

    def remover(self):
        item = Pilha.remover(self)
        self.__soma -= item
        return item

    def getSoma(self):
        return self.__soma

p1 = AdicionandoPilha()

for i in range(20):
    p1.inserir(i)
print("Soma: ", p1.getSoma())

for i in range(10):
    print( "Item removido: ", p1.remover())