chaves = [12,89,45,37,66,23,98,67]

pesquisa = int( input("Chave: ") )
achou = False
for i in chaves:
    if i == pesquisa:
        achou = True

if achou:
    print("Achou")
else:
    print("Não Achou")