'''< Crie uma lista denominada Mat. 
Adicione outras três sub-listas a Mat
Cada sub-lista com os respectivos elementos:
Sublista 1 : 1, 2, 3
Sublista 2: 4, 5, 6 
Sublista 3: 7, 8, 9 

Imprima todos os elementos da primeira linha, utilizando mat dentro do laço 
Imprima todos os elementos numéricos armazenados em mat utilizando laços.>'''

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Elementos da primeira linha")
for elem in mat [0]:
    print(elem, end = " ")
print()    
print("Todos os elementos de mat")
for linha in mat:
    for elem in linha:
        print(elem, end =" ")
    print()
   