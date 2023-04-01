from stats import *
from fight import *
from pokemon import *
import time

def start():
    while True:
        print(' ')
        print('MENU')
        print('1 - Lancer la partie')
        print('2 - Quitter')
        print(' ')
        number = input('Entrer un chiffre > ')
        print(' ')
        if number.isdigit() == False:
            print(' ')
            print('Entrer le chiffre 1 ou 2 !')
            print(' ')
        elif number == "1":
            game()
        elif number == "2":
            break
        else:
            print(' ')
            print('Entrer un chiffre valide !')
            print(' ')

def game():
    my_pokemon = stats()
    my_pokemon.playerpokemon()
    my_pokemon.setstats()
    print("")
    print("-----------------")
    print("")
    print("Ton pokemon")
    my_pokemon.displayPokemon()
    pokemon_random = stats()
    pokemon_random.pokerandom()
    pokemon_random.setstats()
    print("")
    print("Ton adversaire")
    pokemon_random.displayPokemon()

    print("")
    print("Prêt pour le combat ? (Appuyer sur la touche entrée)")
    input()
    
    f = fight(my_pokemon, pokemon_random)
    while my_pokemon.gethp() > 0 and pokemon_random.gethp() > 0:
        print("À ton tour ! Attaque ton adversaire " + pokemon_random.getname() + " avec ton Pokemon " + my_pokemon.getname() + " (Appuyer sur la touche entrée)")
        input()
        f.attack(my_pokemon, pokemon_random)
        print('PV de l\'adversaire ' + pokemon_random.getname() + ' : ' + str(pokemon_random.gethp()))
        print('')
        f.checkWinner()
        if f.winner == True:
            break

        time.sleep(1)
        print("À son tour ! " + pokemon_random.getname() + " vous attaque")
        time.sleep(2)
        f.attack(pokemon_random, my_pokemon)
        print('')
        print('PV de ton pokemon ' + my_pokemon.getname() + ' : ' + str(my_pokemon.gethp()))
        print('')
        time.sleep(2)
        f.checkWinner()
        if f.winner == True:
            break
start()