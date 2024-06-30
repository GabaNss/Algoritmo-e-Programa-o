#variaveis
n1 = 0
n2 = 0
resultado = 0

#função
def somar_numero(num1, num2):
     resultado = num1 + num2
     return resultado

#algoritmo
n1 = int(input("informe o primeiro número: "))
n1 = int(input("informe o segundo número: "))

print(f"A soma dos números é: {somar_numero(n1,n2)}")