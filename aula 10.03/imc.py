peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


imc = peso/(altura ** 2)

print("Seu IMC é igual %.2f"%imc);

if imc < 18.5:
    print("Peso abaixo da média.");

elif imc < 25 and imc >= 18.5:
    print("Peso normal");

elif (imc < 30 and imc>= 25):
    print("Acima do peso ideal");

elif (imc >= 30):
    print("Início de Obesidade");


