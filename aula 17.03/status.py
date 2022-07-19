nota1 = int(input("Nota1: "))
nota2 = int(input("Nota2: "))

media = (nota1+nota2)/2

if media >=7:
    print("Aprovado")
elif media >= 3:
    print("Em exame")
else:
    print("Reprovado")
