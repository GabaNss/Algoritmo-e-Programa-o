#variavei
mat=[[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

#algoritmo
for linha in range (0,5,1):
     for coluna in range (0,5,1):
        mat[linha][coluna] = int(input(f'Informe um número para a posição {linha + 1}, {coluna + 1}: '))
    
for linha in range (0,5,1):
     for coluna in range (0,5,1):
         if(linha == coluna):
            print(f"[{mat[linha][coluna]}]", end= ' ')
         else:
            print("  ", end= ' ')
     print()