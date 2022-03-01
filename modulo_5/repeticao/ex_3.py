#3. Um número primo é um número que é divisível apenas por 1 e por ele mesmo.
# Escreva um programa que receba um número n e informe se esse número é primo ou não.

n = int(input("Digite um numero: \n"))

continuar = "s"

while continuar == "s":
    if n%2 == 0:
        print("O numero ", n," não é impar")

    else:
        print("O numero ", n, " é impar")
    
    continuar = input("Deseja continuar: s/n \n")
    n = int(input("Digite um numero: \n"))
