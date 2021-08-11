msm = input("Digite a sua mensagem")
cripto = ""
descripto = ""

for c in msm:
    c = c.upper()
    codigo = ord(c) + 1
    cripto += chr(codigo)

print("Mensagem Criptografada: "+ cripto)

for c in cripto:
    codigo = ord(c)-1
    descripto += chr(codigo)

print("Mensagem Descriptada: "+descripto)