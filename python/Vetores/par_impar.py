#variaveis
i = 0
vet = [0]*5
vet1 = [0]*5
n = 50
#algoritmo

for i in range(0, n):
     vet[i] = int(input(f"Informe o número para a posição {i+1}: "))

     if(i % 2 != 0):
        vet1[i] = (vet[i]*0.05) + vet[i]
     else:
        vet1[i] = (vet[i]*0.02) + vet [i]

for i in range(0, n):    
    print(f"[{vet[i]}]", end=' ')

print(' ')

for i in range(0, n):    
    print(f"[{vet1[i]}]", end=' ')