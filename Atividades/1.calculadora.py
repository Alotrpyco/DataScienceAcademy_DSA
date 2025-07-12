print("***********************Bem-vindo à calculadora criada por Sérgio Ricardo com o auxílio da DSA****************************")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número: "))
operação = input("Selecione um simbolo de uma operação: (soma(+), subtração(-), divisão(/), multiplicação(*), exponenciação(**): ")
if operação == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)
elif operação == "-":
    resultado = num1 - num2 
    print("resultado é:", resultado)
elif operação == "/":
    resultado = num1/num2
    print("O resultado é:", resultado)
elif operação == "*":
    resultado = num1*num2
    print("O resultado é:", resultado)
elif operação == "**":
    resultado = num1**num2
    print("O resultado é:", resultado)
else:
    print("Erro, pois não foi indentificado nenhuma das operações")
