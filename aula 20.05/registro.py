try:
    arquivo = open("bd.imed","r")
    conteudo = arquivo.read()
    arquivo.close()
    print("Seja bem-vindo novamente ", conteudo)

except:
    nome = input("Informe o nome para registro: ")
    arquivo = open("bd.imed","w")
    arquivo.write(nome)
    arquivo.close

'''
arquivo= open("bd.imed","w")
arquivo.write("Marcos Santos")
arquivo.write("\n")
arquivo.write("IMED")
arquivo.close()
'''
'''
try:
    arquivo = open("bd.imed","r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
except:
    print("Arquivo vazio!")
    arquivo = open("bd.imed","w")
    arquivo.close()

'''