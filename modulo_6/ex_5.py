#5. Suponha o seguinte programa:
# Alunos e suas notas representados através de dicionários
# alunos = [
# {
# "nome": "Alice",
# "nota": 8,
# },
# {
# "nome": "Bob",
# "nota": 7,
# },
# {
# "nome": "Carlos",
# "nota": 9,
# }
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

soma = 0

for aluno in alunos:
    soma += aluno["nota"]

    media = soma / len(alunos)

print(media)