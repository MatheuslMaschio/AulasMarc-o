arquivo = open("nomes.txt","r")
conteudo = arquivo.readlines()
print(conteudo)
arquivo.close()

conteudo[2] = "João\n"

arquivo = open("nomes.txt","w")
arquivo.write( ''.join(conteudo)  ) #escrevendo listas em arquivo
arquivo.close()

