# Curso: desenvolvivento de sistemas
# Turma: 0152
# Autor : Beatriz victoria
# Data do inicio : 19/06/2024
# Data final: 19/06/2024
# Objetivo: criação do login do sistema

# biblioteca do sistema
import os
import platform

# limpando
if platform.system() == 'Windows':
        os.system('cls')
else:
    os.system('clear')


usuario_bd = ""
senha_bd = ""
comfirmacao_bd = ""

while True:
    usuario_bd = str(input('Entre com o nome de usuário: '))
    senha_bd = str(input('Entre com a senha: '))
    comfirmacao_bd = str(input('Digite novamente sua senha: '))

    if (senha_bd != comfirmacao_bd):
        print('Sua senha e confirmação são diferentes!')
        continue
    else:
        break

print(f'-'*79)
print(f'Bem-vindo(a) {usuario_bd}!')

# fazendo o login
while True:
    usuario = str(input('Entre com o nome de usuário: '))
    senha = str(input('Entre com a senha: '))
    comfirmacao = str(input('Digite novamente sua senha: '))

    if (((usuario == usuario_bd) 
         and (senha == senha_bd) 
         and (comfirmacao == comfirmacao_bd))):
        break
    else:
        print('Algum dos seus dados estão incorretos!')

print(f'Bem-vindo(a) {usuario_bd}!')