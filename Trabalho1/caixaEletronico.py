#obrigatório Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
print ("Valor Mínimo de saque:R$10,00");
print ("Valor Máximo de saque:R$:600");

saque = int(input("Informe o valor que devera ser sacado:"));

notaDeCem = int(saque/100);
saque = saque - (notaDeCem*100);

notaDeCinquenta = int(saque/50);
saque = saque - (notaDeCinquenta*50);

notaDeDez = int(saque/10);
saque = saque - (notaDeDez*10);

notaDeCinco = int(saque/5);
saque = saque -(notaDeCinco*5);

notaDeUm = saque;

print("Notas R$1,00 =",notaDeUm);
print("Notas R$5,00 =",notaDeCinco);
print("Notas R$10,00 =",notaDeDez);
print("Notas R$50,00 =",notaDeCinquenta);
print("Notas R$100,00 =",notaDeCem);

