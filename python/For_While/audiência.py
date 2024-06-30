# variaveis
canal = 1
nove = 0
doze = 0
vinte = 0
quarenta = 0
outras = 0
zero = 0
total = 1
# algoritmo
while canal != 0:
    canal = int(input('Informe o canal ( 9 | 12 | 23 | 40 ): '))
    if canal == 9:
        nove += 1

    elif canal == 12:
        doze += 1

    elif canal == 23:
        vinte += 1

    elif canal == 40:
        quarenta += 1

    elif canal == 0:
        zero += 1

    else:
        outras += 1

total = (nove + doze + vinte + quarenta + outras)
nove = (nove/total)*100
doze = (doze/total)*100
vinte = (vinte/total)*100
quarenta = (quarenta/total)*100
outras = (outras/total)*100

print(f'O canal 9 tem a audiência de {nove}%')
print(f'O canal 12 tem a audiência de {doze}%')
print(f'O canal 23 tem a audiência de {vinte}%')
print(f'O canal 40 tem a audiência de {quarenta}%')
print(f'Os outros canais tem a audiência de {outras}%')
