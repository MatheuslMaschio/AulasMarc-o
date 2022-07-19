# obrigatório Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média
conceito = ""
notaMensal = float(input("Digite a nota mensal:"));
notaTrimestral = int(input("Informe a Nota Trimestal:"));

media = (notaMensal + notaTrimestral)/2

if media >=9 and media<=10:
    conceito = "A"
    print("Média= %.2f ==> Conceito = %s" %(media,conceito));
elif media >= 7.5 and media <=9:
    conceito = "B"
    print("Média= %.2f==> Conceito = %s" %(media, conceito));
elif media >= 6 and media <=7.5:
    conceito = "C"
    print("Média= %.2f==> Conceito = %s" %(media, conceito));
elif media >= 4 and media <=6:
    conceito = "D"
    print("Média= %.2f==> Conceito = %s" %(media, conceito));
else:
    conceito = "E"
    print("Média= %.2f==> Conceito = %s" %(media, conceito));


