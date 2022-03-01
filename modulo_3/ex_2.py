#2-Escreva um programa com as seguintes especificações:
# Uma variável “valor_compras” que receba um valor do tipo float, representando o valor total das compras.
# Uma variável “desconto” que receba um valor do tipo float, representando o desconto a ser aplicado sobre o valor total das compras.
# Uma variável “quantidade_itens”, que represente a quantidade de itens que foram comprados.
# Seu programa deve imprimir dois resultados:
#1. O valor final das compras, considerando o desconto aplicado.
#2. O custo médio de cada item (considerando o valor final das compras).

valor_compras = 1000.50
desconto = 0.2 #20%
quantidade_itens = 30

valor_final = valor_compras * desconto
custo_medio = valor_final / quantidade_itens

print(round(valor_final))#valor arredondado
print(round(custo_medio))#valor arredondado