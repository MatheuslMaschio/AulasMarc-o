###### Faça um programa para a leitura de duas notas parciais de um aluno. -Opcional
notaMensal = int(input("Informe a Nota Mensal:"));
notaTrimestral = int(input("Informe a Nota Trimestal:"));

media = (notaMensal + notaTrimestral)/2;

if media >= 7: 
    print("Você está aprovado!!");
elif media < 7:
    print("Você está em exame!!");
else:
    print("Você foi aprovado com distinção!!");

