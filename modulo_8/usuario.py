class Usuario():
    qtd = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.qtd = Usuario.qtd
        Usuario.qtd += 1

    def imprime_usuario(self):
        print(f'Usuario {self.nome}, email {self.email}')
