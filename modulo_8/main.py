from usuario import Usuario
from administrador import Administrador

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin","admin@exemplo.com",'Administrador')
u.imprime_usuario() # => "Gabriel (gabriel@exemplo.com)
a.imprime_usuario() # => "Admin (admin@exemplo.com) – Administrador"
print(Usuario.qtd) # => 2