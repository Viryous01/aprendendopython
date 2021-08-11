class Classy:
    def outra(self):
        print("outra")
    def metodo(self):
        print("Método")
        self.outra()

obj = Classy()
obj.metodo()