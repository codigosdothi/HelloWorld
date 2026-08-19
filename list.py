'''< Declare uma lista vazia. Em seguida solicite ao usuário que informe 5 elementosque serão armazenados na lista. 
Utilize o append()
Calcule a média entre elementos da lista e mostre o resultado na tela.
Imprima o contéudo de cada um' dos elementos da lista, indivudulamente na tela> '''

v = []
s = 0

for i in range(5):
    dado = int(input("Digite um número inteiro: "))
    v.append(dado)
    s += dado
    
media = s / 5

for elem in v:
    print(elem, end=" ") 
    
print(f"Média dos elementos: {media}")