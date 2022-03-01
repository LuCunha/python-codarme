#2. Escreva um programa que receba um número inteiro n e imprima todos os números pares de 1 até n (inclusive n ).

final = int(input("Digite o numero da função: \n"))
i = 1

while i <= final:
    if i%2 == 0:
        print(i)
    i += 1