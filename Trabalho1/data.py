#obrigatório Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
varAno = int( input( "Ano:"));
varMes = int( input("Mes:"));
varDia = int( input("Dia:"));

validar = False

#Meses com 31 dias
if(varMes==1 or varMes==3 or varMes==5 or varMes==7 or varMes==8 or varMes==10 or varMes ==12):
    if(varDia<=31):
        validar = True
#Meses com 30 dias
elif(varMes == 4 or varMes==6 or varMes==9 or varMes==11):
    if(varDia<=30):
        validar = True
elif varMes == 2:
    #Testa se é Bissexto
    if(varAno%4==0 and varAno%100!=0) or (varAno%400 == 0):
        if(varDia <= 29):
            validar = True
        elif(varDia <=28):
            validar = True

if(validar):
    print("Data Válida!!");
else:
    print("Data Inválida");

