#3. Escreva um programa de autenticação que receba um nome de usuário e senha ( input ) informe se:
# Autenticação foi bem-sucedida.
# Se o nome de usuário não existe.
# Se a senha está incorreta.
# Os valores corretos de nome de usuário e senha devem estar armazenados em constantes, como no exemplo abaixo:
# USUARIO = "admin"
# SENHA = "123123"
# nome_usuario = input("Digite o nome do usuário: "\n)

usuario = "admin"
senha_salva="123123"

nome = input("Digie o nome de usuário: \n").lower()
senha = input("Digite a senha: \n")

#print(nome)

if (nome == usuario) and (senha == senha_salva):
    print("Autenticação foi bem-sucedida.")

elif(nome != usuario) and (senha == senha_salva):
    print("O nome de usuário não existe.")

elif(nome == usuario) and (senha != senha_salva):
    print("A senha está incorreta.")

else:
    print("Ambos os dados estão incorretos.")
