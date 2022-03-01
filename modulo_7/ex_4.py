#4. Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma tupla quanto 
# um dicionário. Dica: método type pode te ajudar

def maior_idade(pessoa):

    if type(pessoa) == tuple:
        nome, idade = pessoa

        if idade >= 18:
            return ("Tuple : maior de idade")
        else:
            return ("Tuple: menor de idade")

    elif type(pessoa) == dict:
        idade = pessoa["idade"]

        if idade >= 18:
            return ("Dicionário : maior de idade")
        else:
            return ("Dicionário: menor de idade")

    
nome = input('Digite um nome: \n')
idade = int(input("Digite uma idade: \n"))    

pessoa_tuple = (nome, idade)
idade_tuple = maior_idade(pessoa_tuple)
print(idade_tuple)

pessoa_dict = {

    'nome': nome,
    'idade': idade

}

idade_dict = maior_idade(pessoa_dict)
print(idade_dict)