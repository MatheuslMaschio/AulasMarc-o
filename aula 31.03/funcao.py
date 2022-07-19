#### back-end
def somar(n1, n2):
    soma = n1 + n2
    return soma

def convertCaps(texto):
    return texto.upper()
#################################################
#### front-end
nome = convertCaps( input("Nome")  )
print(nome)
print( somar(8, 9) )
print( somar(67, 45) )
print( somar(6, 1) )


