tanque = 200
print("Litros:", tanque)
while tanque > 0 :
    retirada = int( input("Quantos litros :") ) 
    if retirada <= tanque:
        tanque = tanque - retirada
        print("Sobrou",tanque,"litros")
    else:
        print("Não temos essa quantidade!")