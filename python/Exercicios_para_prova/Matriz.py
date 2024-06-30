# Variaveis
matriz=[[0]*3, [0]*3, [0]*3]
matriz1=[[0]*3, [0]*3, [0]*3]

# Algoritmo

# Inserindo valor na matriz
for i in range (0,3):
    for j in range (0,3):
            
             matriz1[i][j]= int(input(f'Insira um valor inteiro entre 1-9 na casa [{i + 1}][{j + 1}]: '))
             if(matriz1[i][j] <= 9 ) and (matriz1[i][j] >= 1):
                matriz[i][j] = matriz1[i][j]
             else:
              print('É só entre 1 e 9 burro!!!')
# Imprimindo a matriz
for i in range (0,3):
    for j in range (0,3):
         print(f"[{matriz[i][j]}]", end= ' ')
    print() 
    