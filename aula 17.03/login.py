import os
os.system("cls")
os.system("color 7")  # muda para a cor branca

usuario = input("Usuário: ")
senha = input("Senha: ")

# Usuario: admin Senha: 123

if usuario == "admin" and senha == "123":
    print("Acesso Permitido")
else:
    print("Usuário ou Senha Inválida")
    exit()

###################################################
os.system("color 2")
print("Bem-Vindo ao Sistema Briquilaus!")
