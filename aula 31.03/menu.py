import os
import time
while True:
    os.system("cls")
    print("Escolha uma opção: ")
    print("(1) Português")
    print("(2) Inglês")
    print("(3) Espanhol")
    print("(0) Sair")
    op = input()
    if op == "1":
        print("bom dia\n")
    elif op == "2":
        print("good morning\n")
    elif op == "3":
        print("buenos dias\n")
    elif op == "0":
        break
    else:
        print("Opção Inválida!\n")
    #input("press to continue....")
    time.sleep(5)