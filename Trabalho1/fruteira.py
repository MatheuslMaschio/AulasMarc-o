#obrigatório Uma fruteira está vendendo frutas com a seguinte tabela de preços:

varMorangos = int(input("Digite a quantidade de morangos [kg]: "));
varMacas = int(input("Digite a quantidade de maças[kg]: "));

precoMorango = varMorangos * 2.50
precoMorango2 = varMorangos * 2.20

precoMaca = varMacas * 1.80
precoMaca2 = varMacas * 1.50

print("quantidade de maças: ", varMacas, "\nQuantidade de morangos: ", varMorangos);

if varMorangos > 5:
    precoCertoMo = precoMorango;
else:
    precoCertoMo = precoMorango2;

if varMacas > 5:
    precoCertoMa = precoMaca;
else:
    precoCertoMa = precoMaca2;

precoTotal = precoCertoMa + precoCertoMo;

if precoTotal > 25 or (varMacas + varMorangos) > 8:
    print("Preço final: ", (precoTotal - (precoTotal * 0.1)));
else:
    print("Preço final: ", precoTotal);