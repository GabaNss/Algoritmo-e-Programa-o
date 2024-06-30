#Função
def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial
#Variaveis
n = 0 

#Algoritmo
n = int(input(f'Insira um número para calcular seu fatorial: '))

print (f'{fatorial(n)}')
      