#1. Escreva uma função que recebe um número inteiro positivo e retorna True caso ele seja primo e False , caso contrário.

def primo(valor):

    pos = 0

    for number in range(1, valor + 1):
        if valor % number == 0:
            pos += 1
    
    if pos == 2:
        return True
    else:
        return False

number = int(input("Digite um numero inteiro positivo: \n"))
valor = primo(number)
print(valor)