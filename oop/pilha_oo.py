class Pilha:
    def __init__(self):
        self.__minha_pilha = []

    def inserir(self, item):
        self.__minha_pilha.append(item)
        print("Estado da pilha: ", self.__minha_pilha)

    def remover(self):
        item = self.__minha_pilha[-1]
        del self.__minha_pilha[-1]
        print("Elemento removido: ", item + "\nEstado da pilha: ", self.__minha_pilha)


p1 = Pilha()
p1.inserir("A")
p1.inserir("V")
p1.inserir("F")
p1.inserir("C")

p1.remover()