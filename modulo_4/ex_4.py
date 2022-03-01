#4. Alice é responsável por escrever um programa que verifica se um cupom de 
# desconto pode ser utilizado. O programa recebe 3 valores e retorna True caso o 
# cupom possa ser utilizado, ou False , caso contrário. 
# Os três valores que o programa recebe são: 
# 1. Valor de compra (float) 
# 2. Valor do frete (float) 
# 3. Cliente é cadastrado no programa de fidelidade (string “s” (sim) ou “n” (não)) 
# O cupom tem a seguinte regra: 
# Caso o valor da compra somado ao frete seja superior a R$ 100, ou o cliente seja cadastrado no programa de fidelidade, o 
# cupom de desconto pode ser utilizado. Caso contrário, o cupom não pode ser utilizado.
# Seu objetivo é implementar o programa que atenda a especificação acima.

compra = float(input('Digite o valor da compra:\n'))
frete = float(input('Digite o valor do frete:\n'))
fidelidade = input('s -  Sim , n - Não\n')

if (compra + frete > 100) or (fidelidade == 's'):
    print('O cupom de desconto pode ser utilizado')

else:
    print('O cupom não pode ser utilizado')


