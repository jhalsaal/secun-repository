import random

def options():
    computer_list = ["piedra", "papel", "tijera"]
    computer_option = random.choice(computer_list)
    print("Ingresa una opcion: piedra, papel o tijera")
    user_option = input("===>")
    user_option = user_option.lower()
    if not user_option in computer_list:
        return '', 0, '', 0, False
    index_computer = computer_list.index(computer_option)
    index_user = computer_list.index(user_option)
    return computer_option, index_computer, user_option, index_user, True

def winner_game(index_computer,computer_wins, index_user,usser_wins,counter):
    diference = abs(index_computer - index_user)
    if index_computer == index_user:
        print("¡Empate!")
    elif (diference == 1 and index_computer > index_user) or (diference == 2 and index_computer < index_user):
        computer_wins += 1
    else: 
        usser_wins +=1
    counter +=1
    return computer_wins, usser_wins, counter

def game():
    counter = 1
    computer_wins = 0
    usser_wins = 0
    while computer_wins <2 and usser_wins <2:
        print("*******Ronda********: ", counter)
        computer_option,index_computer, user_option, index_user, validation  = options()
        if validation== False:
            print("Opcion no valida, ingresa una opcion valida perro")
            continue
        computer_wins, usser_wins, counter =  winner_game(index_computer,computer_wins,index_user,usser_wins,counter) 
        print("La opcion de la maquina es: ", computer_option)
        print("La opcion del usuario es: ", user_option)
        print("La maquina tiene ", computer_wins, " ganadas")
        print("El usuario tiene ", usser_wins, " ganadas")

game()
