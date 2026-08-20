'''< Crie um programa que peça para o usuário preencher o conteúdo de uma matriz de dimensões 3x4.
Após inseridos os dados, realize uma busca na matriz e informe quais valores das linhas e colunas (posição) do maior e do menor elemento de toda matriz>'''


mat = []
for i in range(3):
    linha = []  
    
    for j in range(4):
        numero = int(input("Digite um número"))
        linha.append(numero)
    
    mat.append (linha)
    
print ()
for linha in mat:
    for elem in linha:
        print(elem, end =" ")
    print()

maior_valor = mat[0][0]
linha_maior = 0
coluna_maior = 0

menor_valor = mat[0][0]
linha_menor = 0
coluna_menor = 0

# --- A BUSCA ---
# Percorrendo a matriz inteira novamente
for i in range(3):
    for j in range(4):
        
        # Se acharmos um número MAIOR que o nosso atual 'maior_valor'
        if mat[i][j] > maior_valor:
            maior_valor = mat[i][j]
            linha_maior = i
            coluna_maior = j
            
        # Se acharmos um número MENOR que o nosso atual 'menor_valor'
        if mat[i][j] < menor_valor:
            menor_valor = mat[i][j]
            linha_menor = i
            coluna_menor = j

# --- MOSTRANDO OS RESULTADOS ---
print("\n--- RESULTADOS DA BUSCA ---")
print(f"O MAIOR valor é {maior_valor} e está na linha {linha_maior}, coluna {coluna_maior}.")
print(f"O MENOR valor é {menor_valor} e está na linha {linha_menor}, coluna {coluna_menor}.")