# Variaveis

matriz = [[0]*5,[0]*5,[0]*5]
matrizfalha = [[0]*5,[0]*5,[0]*5]
linha = [0]*3
coluna = [0]*3
n = 0
m = 0

# Algoritmo

# Imprimindo a matriz
for i in range (0, 3):
     for j in range (0, 5):
         print(f'[{matriz[i][j]}]', end= ' ')
     print()

#Estrutura de repetição para inserir os erros
while(n != 'N'):

# Inserindo as casas falhas na matriz
    
        linha = int(input(f'Escolha a linha de um matriz 3x5 para inserir o erro: '))
        coluna = int(input(f'Escolha a coluna de uma matriz 3x5 para inserir o erro: '))
        matriz[linha-1][coluna-1] = 1

        n = input('Você quer inserir mais um erro [S/N]: ').upper()
        i += 1
        if(i == 7):
            n = 'N'

# Imprimindo a matriz
for i in range (0, 3):
    for j in range (0, 5):
        print(f'[{matriz[i][j]}]', end= ' ')
    print()

print(f'A quantidade de erros foi {i}')





