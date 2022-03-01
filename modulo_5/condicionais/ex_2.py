#2. Implemente uma calculadora que recebe 3 valores do usuário:
# a. Operando a (pode ser um inteiro ou float).
# b. Operando b (pode ser um inteiro ou float).
# c. Operador op .
# i. op pode ser uma string representando o operador, por exemplo, "+" ou "-
# ". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para subtração , etc.
# O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o 
# programa deve imprimir uma mensagem: “Não é possível realizar divisão por zero!”

a = float(input("Digite o primeiro numero: \n"))
b = float(input("Digite o segundo numero: \n"))
op = input("Digite qual operação quer realizar: + , -, * ou / \n")

if op == "+":
    print("O resultado da operação é: ", a + b)

elif op == "-":
    print("O resultado da operação é: ", a - b)

elif op == "*":
    print("O resultado da operação é: ", a * b)

elif op == "/":
    print("O resultado da operação é: ", a / b)

else:
    print("Essa não é uma operação valida, tente novamente")