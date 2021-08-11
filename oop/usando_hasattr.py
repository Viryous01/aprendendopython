class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

exampleObject = ExampleClass()

#Verifica se o Objecto contém o atributo b (True)
print(hasattr(exampleObject, 'b'))
#Verifica se o Objecto contém o atributo a (True)
print(hasattr(exampleObject, 'a'))

#Verifica se a Class contém o atributo b (False)
print(hasattr(ExampleClass, 'b'))

#Verifica se a Class contém o atributo a (True)
print(hasattr(ExampleClass, 'a'))