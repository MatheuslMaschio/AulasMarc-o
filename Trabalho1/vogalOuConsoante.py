######## Faça um Programa que verifique se uma letra digitada é vogal ou consoante. - Opcional

listaVogais = ["a","e","i","o","u"];
listaConsoante = ["b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","z"];

informeLetra = input("Informe uma letra:");

if informeLetra in listaVogais:
    print("A letra informada é uma vogal!!");
elif informeLetra in listaConsoante: 
     print("A letra informada é uma consoante!!");
else:
    print("Não é uma letra!!!");
