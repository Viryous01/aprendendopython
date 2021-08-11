try:
    x=int(input("Insira um valor: "))
    y = 1000/x
    print(y)
except ZeroDivisionError:
    print("Insira um valor diferente de Zero")