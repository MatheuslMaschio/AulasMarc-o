#obrigatório Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 

pontos = 0

print("Responda as 5 perguntas com sim ou não");

varA = str(input("Telefonou para a vítima?")).lower;

if varA == "sim":
    pontos = pontos + 1

else:
    pontos = pontos + 0

varB = str(input("Esteve no local do crime?")).lower;

if varB == "sim":
    pontos = pontos + 1

else:
    pontos = pontos + 0

varC = str(input("Mora perto da vítima?")).lower;

if varC == "sim":
    pontos = pontos + 1

else:
    pontos = pontos + 0

varD = str(input("Devia para a vítima?")).lower;

if varD == "sim":
    pontos = pontos + 1

else:
    pontos = pontos + 0

varE = str(input( "Já trabalhou com a vítima?")).lower;

if varE == "sim":
    pontos = pontos + 1

else:
    pontos = pontos + 0

print();

print("Seu nivel de suspeita é ", pontos);

if pontos == 2:
    print("Classificado como: Suspeito!");

if pontos == 3 or pontos == 4:
    print("Classificado como: Suspeito!");

if pontos == 5:
    print("Classificado como: Assasino");

elif pontos == 0:
    print("Classificado como: Inocente");

