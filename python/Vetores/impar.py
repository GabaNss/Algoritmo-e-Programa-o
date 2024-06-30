#variaveis
vet = [0]*30

#algoritmo

for i in range (0, 30):
     vet[i] = int(input(f"Informe o número para a posição {i+1}: "))

for i in range (1, 30, 1):
    if(i % 2 != 0):
        
        print(f" [{vet[i]}] ")