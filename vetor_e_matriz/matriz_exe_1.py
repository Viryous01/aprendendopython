matriz = [[16,10,13,15], [14,16,15,13], [5,15,16,16], [15,1,14,16]]
linha = coluna= soma= media= qte =0
l_menor = l_maior=c_menor=c_maior = 0
num_maior=matriz[0][0]
num_menor=matriz[0][0]
par = []
q_par = 0
impar = []
q_impar = 0

maior_q_media = []
dp = []
ds= []
t_linha = []
s_coluna = []
s_linha = []
matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# 1 - Exibição da Matriz
print("1 - Exibição da matriz")
for linha in range(len(matriz)):
    print()
    for coluna in range(len(matriz)):
        #print("")
        #2 - Cálculo da soma
        soma = soma + matriz[linha][coluna]
        media = soma/(len(matriz)*len(matriz))
        #4 - Pegar os elementos da diagonal Principal
        if linha==coluna:
            dp.append(matriz[linha][coluna])
        if coluna-linha==3:
            ds.append(matriz[linha][coluna])
        if linha==1 and coluna==1:
            ds.append(matriz[linha][coluna+1])
        if linha==2 and coluna==2:
            ds.append(matriz[linha][coluna-1])
        if linha-coluna==3:
            ds.append(matriz[linha][coluna])

        # 6 - Pegar os elementos da Terceira Linha
        if linha==2:
            t_linha.append(matriz[2][coluna])
        # 7 - Pegar os elementos da Seguna Coluna
        if coluna == 1:
            s_coluna.append(matriz[linha][1])
        #11 - Pegar os elementos pares e ímpares
        if matriz[linha][coluna]%2==0:
            par.append(matriz[linha][coluna])
            q_par +=1
        else:
            impar.append(matriz[linha][coluna])
            q_impar +=1

        #12 - Elementos da segundo linha
        if linha==1:
            s_linha.append(matriz[linha][coluna])
        #1 - Exibição da Matriz
        if coluna ==0:
            print("-------------------------")
            print(linha+1, " | ", matriz[linha][coluna], end=" | ")
        elif coluna ==1:
            print(matriz[linha][coluna], end=" | ")
        elif coluna ==2:
            print(matriz[linha][coluna], end=" | ")
        else:
            print(matriz[linha][coluna], end=" | ")

 # 8 Valor maior e menor que a média
for i in range(len(matriz)):
    for j in range(len(matriz)):
        # 10 - Multiplicação dos elementos da matriz por 2
        matriz2[i][j]=(matriz[i][j] * 2)

        if matriz[i][j] > media:
            maior_q_media.append(matriz[i][j])
            qte += 1
        # 9 - Posição do maior e do menor número da matriz
        #Maior valor
        if num_maior < matriz[i][j]:
            num_maior = matriz[i][j]
            l_maior = i
            c_maior = j
        #Menor Valor
        if num_menor > matriz[i][j]:
            num_menor = matriz[i][j]
            l_menor = i
            c_menor = j

# 2 - Exibição da soma
print("\n")
print("2 - A Soma dos Elementos é: ", soma)

#3 - Cálculo apresentação da média
print("3 - A média é: ", media)

#4 Elementos da Diagonal Principal
print("4 - Elementos da Diagonal Principal: ", dp)
#5 Elementos da Diagonal Principal
print("5 - Elementos da Diagonal Secundária: ", ds)
#6 - Elementos da Terceira Linha
print("6 - Elementos da terceira linha: ", t_linha)
#7 - Elementos da Seguna Coluna
print("7 - Elementos da Segunda: ", s_coluna)
#8 - Elementos da Seguna Coluna
print("8 - Quantidade de números maiores que a média: ",qte," Valores maiores que a média : ", maior_q_media)

#9 - Posição do maior e do menor valor
print("9 - O maior valor é: ", num_maior, " e sua posição é: linha ", l_maior, " e coluna ", c_maior,
      "\n O menor valor é: ",num_menor, "e sua posição é: linha ", l_menor, "coluna ", c_menor)

#10 - Multiplicação dos elementos da matriz por 2
print("10 - Multiplicação da matriz por 2: ")
for i in range(len(matriz2)):
    print()
    for j in range(len(matriz2)):
        if j==0:
            #print(j, end=" | ")
            print("-------------------------")
            print(i+1,"|", matriz2[i][j], end=" | ")
        if j == 1:
            print(matriz2[i][j], end=" | ")
        if j == 2:
            print(matriz2[i][j], end=" | ")
        if j == 3:
            print(matriz2[i][j], end=" | ")

#11 - Elementos pares e ímpares e suas quantidades
print("\n")
print("11 - Quantidade par: ", q_par, " Elementos: ", par, "\n Quantidade ímpar: ", q_impar, " Elementos: ", impar)

#12 - Elementos da segunda linha
print("12 - Elementos da segunda linha: ", s_linha)