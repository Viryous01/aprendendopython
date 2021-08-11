pilha = []

def inserir(item):
    pilha.append(item)

def remover():
    item = pilha[-1]
    del pilha[-1]
    print("Item removido: "+ item)

inserir("A")
print(pilha)
inserir("V")
print(pilha)
inserir("C")
print(pilha)

remover()
print(pilha)