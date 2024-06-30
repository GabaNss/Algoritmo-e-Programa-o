#variaveis
i = 0
vet = [0]*10

#algoritmo

for i in range (0,10,1):
     vet[i] = int(input(f"Informe o número para a posição {i}: "))

for i in range (9, -1, -1):
    print(f" [{vet[i]}] ", end= ' ')