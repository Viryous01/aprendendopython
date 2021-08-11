try:
    y = 1/0
except ZeroDivisionError:
    print("Impossível divisão por Zero")
except ArithmeticError:
    print("Erro de aritmetica")
print("Fim")
