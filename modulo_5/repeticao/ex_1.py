#1. Escreva um programa que receba um número inteiro n e imprima a soma de todos os números de 1 até n (inclusive n ).

final = int(input("Digite o numero da função: \n"))
i = 1

while i <= final:
    print(i, " + ", final, " = ", i + final)
    i += 1
