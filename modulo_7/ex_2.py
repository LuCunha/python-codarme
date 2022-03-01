#2. Implemente uma função que recebe uma lista de números inteiros e retorna uma 
# tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num é o valor desse número.

def listas(list_numb):
    
    pos = 0
    num = 0

    for posicao in range(0, len(list_numb)):
        
        if list_numb[posicao] > num:
            num = list_numb[posicao]
            pos=posicao

    return (pos, num)
        

number = [20,2,130,500]
list_numb = listas(number)
print(list_numb)  


        

