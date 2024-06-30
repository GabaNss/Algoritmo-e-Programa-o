sidade = 0
mulher = 0
homem = 0
velho = 0
velha = 0
media = 0
#algoritmo
for i in range (1,21):
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o genero (H) para homem e (M) para mulher: ').upper()

    if (i == 20):
        print('A turma está lotada!!!')

    sidade = sidade + idade

    if (sexo == 'M'):
        mulher += 1

    if (sexo == 'M') and (idade >= 18):
        velha += 1
    elif (sexo == 'H') and (idade >= 18):
        velho += 1
media = sidade / 20

print (f'A idade média dos candidatos é: {media}')
print (f'A quantidade de mulheres inscritas é: {mulher}')
print (f'A quantidade de homens adultos é {velho} e a quantidade de mulheres adultas é {velha}')
