#variaveis
n = 0

#algoritmo

n = int(input(f'Insira o a nota entre 0-100: '))

if(n <= 100 ) and (n >= 90):
    print('A')
    
if(n <= 89) and (n >= 80):
    print('B')
    
if(n <= 79) and (n >= 70):
    print('C')
    
if(n <= 69) and (n >= 60):
    print('D')
    
if(n <= 59) and (n >= 0):
    print('F')

else:
    print('Fala o número certo poha!!!')