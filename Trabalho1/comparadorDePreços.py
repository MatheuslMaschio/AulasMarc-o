#obrigatório Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

valor1 = int(input("Insira o valor do primeiro produto:"));
valor2 = int(input("Insira o  valor do segundo produto:"));
valor3 = int(input("Insira o valor do terceiro produto:"));

if (valor1 < valor2 and valor1 < valor3):
    print("O primeiro produto é o mais barato!!");

elif (valor2 < valor1 and valor2 < valor3):
    print("O segundo produto é o mais barato!!");

else:
    print("O terceiro produto é o mais barato!!");
