#variaveis
somaidade = 0
maior = 0
menor = 0

#algoritmo
n = int(input("Digite a quantidade de pessoas para inserir a idade: "))

for i in range (1, n+1):

    idade = int(input("Informe a idade: "))
    somaidade = idade + somaidade
    old = idade
    if (idade >= maior):
        maior = idade
    if (idade <= menor):
        menor = idade
    elif ( menor == 0):
        menor = idade

media = somaidade / n

print (f'{n} pessoas foram escolhidas para falarem sua idade, a média de idade entre elas é {media:.2f}, a maior idade é {maior} e a menor é {menor}')


    