from sqlite3 import adapt
from usuario import Usuario

class Administrador(Usuario):
    
    def __init__(self, nome, email, acesso):
        super().__init__(nome, email)
        self.acesso = acesso

    def imprime_usuario(self):
        print(f'Usuário: {self.nome}, e-mail: {self.email} - {self.acesso}')
