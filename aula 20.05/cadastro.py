# no cadastro -> não pode ter espaço no primeiro caracter
# no cadastro -> nome não pode ter menos de 2 caracteres
# deletar -> informar ID que não existe
# listar -> se for vazio o Array mostrar que não tem registro
# no cadastro -> nomes russos -> informar caracter inválido
# na exclusão -> Id inválido -: msg correta
# na exclusão -> números maiores ou igual a 1
def lerConteudo():
    arquivo = open("data.dat","r")
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

def lerConteudoEmLista():
    arquivo = open("data.dat","r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo

def escreverConteudo(conteudo):
    arquivo = open("data.dat","w")
    arquivo.write(''.join(conteudo))
    arquivo.close()

def criarArquivo():
    arquivo = open("data.dat","w")
    arquivo.close()

import os
while True:
    os.system("cls")
    print("(1) Cadastro")
    print("(2) Registros")
    print("(3) Deletar")
    print("(0) Sair")
    op = input()
    if op == "1":
        conteudo = []
        try:
            conteudo = lerConteudoEmLista()
        except:
            criarArquivo()
        nome = input("Informe o nome para registro: ")
        conteudo.append(nome+"\n")
        escreverConteudo(conteudo)
        print("Registro Salvo com Sucesso!")
        input()
    elif op == "2":
        try:
            conteudo = lerConteudo()
            print(conteudo)
            input()
        except:
            print("nenhum registro encontrado!")
            input()
    elif op=="3":
        try:
            conteudo = lerConteudoEmLista()
            for id,item in enumerate(conteudo):
                print(id, "-",item)
            idDeletar = int(input("Informe o ID que deseja excluir: "))
            del conteudo[idDeletar]
            escreverConteudo(conteudo)
            print("Registro excluído com sucesso!")
            input()
        except:
            print("Nenhum registro encontrado!")
            input()
    
    elif op=="0":
        break
    else:
        print("Opção Inválida!")
        input()
