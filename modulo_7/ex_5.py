# 5. Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
# retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
# é permitido utilizar o método in .

def arg(valores, elemento):

    retorno = False

    for valor in valores:
        if valor == elemento:
            retorno = True

    return retorno

valores = [1, 2, 3, 4, 5, 6]
elemento = 6
result = arg(valores, elemento)
print(result)
