'''<Crie um código-fonte que importe as bibliotecas math e os. 
Utilize funções destas bibliotecas para demonstrar seu uso.
Utilize ao menos 2 funções nativas do Python no seu código.>'''


import math
import os 

# exemplos de uso da biblioteca math
x = 81 
raiz_quadrada = math.sqrt(x)
print(f"A raiz quadrada de {x} é {raiz_quadrada}")

angulo = 45
seno = math.sin(angulo)
print("O seno de {} graus é {:.2f}".format(angulo, seno))


# exemplos de uso da biblioteca os
diretorio = os.getcwd()
print(f"O diretório atual corrente é: {diretorio}")

# os.system ("cls") 

#exemplos de funções nativas do Python
lista = [110, 220, 330]
tamanho_lista = len(lista)
print(f"O tamanho da lista é: {tamanho_lista}")

soma = sum(lista)
print(f"A soma dos elementos da lista é: {soma}")
