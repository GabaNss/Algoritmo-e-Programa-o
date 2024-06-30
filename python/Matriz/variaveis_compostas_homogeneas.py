#variavei
mat=[[0]*3, [0]*3, [0]*3]

#algoritmo
for linha in range (0,3,1):
     for coluna in range (0,3,1):
        mat[linha][coluna] = int(input(f'Informe um número para a posição {linha + 1}, {coluna + 1}: '))
    
for linha in range (0,3,1):
     for coluna in range (0,3,1):
         print(f"[{mat[linha][coluna]}]", end= ' ')
     print()