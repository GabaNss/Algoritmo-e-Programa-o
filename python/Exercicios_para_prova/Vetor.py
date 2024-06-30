# Variaveis
vetor = [0]*5
media = 0
menor = 0
maior = 0
soma = 0
# Algoritmo

for i in range(0,5):
    vetor[i] = int(input(f'Insira o valor na casa [{i + 1}]: '))

    if (maior < vetor[i]):
        maior = vetor[i]
    
    if (i == 0):
        menor = vetor[i]
    
    if (menor > vetor[i]):
        menor = vetor[i]
        
    soma += vetor[i]

media = soma/5
    
        
print (f'O maior valor é...: {maior}')
print ()
print (f'O menor valor é...: {menor}')
print ()
print (f'O valor da soma é.: {soma}')
print ()
print (f'O valor da media é: {media}')