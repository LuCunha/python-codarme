#3. Implemente uma função maior_idade(pessoa) que receba uma tupla representando
# uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou não.

def maior_idade(pessoa):
    
    if pessoa[1] >=18:
        maior = "Sim"
    else:
        maior = "Não"

    return maior

    
pessoa = ("Lucas", 23)
nome, idade = pessoa
print(nome, "é maior de idade? ", maior_idade(pessoa), " ele tem ", idade, " anos")


       


