#4. O jogo “Acerte o número” funciona da seguinte maneira:
# a. Existe um certo número inteiro declarado dentro do programa que o usuário desconhece. Por exemplo: numero = 8
# b. O usuário tem 3 tentativas para acertar o número.
# c. A cada tentativa, é informado ao usuário se o número que ele digitou é maior, menor, ou igual ao número correto.
# d. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário acerta o número (ganhou).
# Implemente o jogo “Acerte o número”.

numero_sorte = 8
tentativas = 1

while tentativas <= 3:
    chute  = int(input("Digite seu chute: \n"))
    if chute == numero_sorte:
        print("Você acertou!")
        break
    elif chute < numero_sorte:
        print("Seu chute ", chute, " é menor que o numero da sorte" )
    else:
        print("Seu chute ", chute," é maior que o numero da sorte" )

    tentativas += 1
    
    if tentativas == 4:
        print("Acabaram suas tentativas")
        break
