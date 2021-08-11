class Exemplo:
    contador = 0
    def __init__(self, val=1):
        self.__primeiro = val
        Exemplo.contador +=1

e1 = Exemplo()
e2 = Exemplo(2)
e3 = Exemplo(4)

print(e1.__dict__, e1.contador)
print(e2.__dict__, e2.contador)
print(e3.__dict__, e3.contador)

#=============================================================
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 2

exampleObject = ExampleClass(3)

try:
    print(exampleObject.a)
except AttributeError:
    pass
#hasattr função para verificar a existência de um atributo de um objecto
if hasattr(exampleObject, 'b'):
    print(exampleObject.b)

#==============================================================