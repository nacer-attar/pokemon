from pokemon.pokemon import *

class fight (Pokemon):
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.winner = False

 # Fonction d'ataque, avec l'attaquant et la victime en arg
    def attack(self, attacker, victim):
        result = 0
        if "Eau" in attacker.type and "Feu" in victim.type or "Feu" in attacker.type and "Plante" in victim.type or "Plante" in attacker.type and "Eau" in victim.type :
            result = (victim.gethp() + victim.defense) - (attacker.attack * 2)
        elif "Eau" in attacker.type and "Plante" in victim.type or "Feu" in attacker.type and "Eau" in victim.type or "Plante" in attacker.type and "Feu" in victim.type  :
            result = (victim.gethp() + victim.defense) - (attacker.attack * 0.5)
        elif "Normal" in attacker.type and "Eau" in victim.type or "Normal" in attacker.type and "Feu" in victim.type or "Normal" in attacker.type and "Plante" in victim.type:
             result = (victim.gethp() + victim.defense) - (attacker.attack * 0.75)
        else: 
            result = (victim.gethp() + victim.defense) - (attacker.attack)
        if result <= 0:
            victim.setPV(0)
        else:
            victim.setPV(result)
    
    def checkWinner(self): 
        if self.pokemon1.gethp() == 0:
            print(self.pokemon1.getname() + " n'est plus capable de se battre...  " + self.pokemon1.getname() + "a gagné")
            print(" ")
            self.winner = True
        elif self.pokemon2.gethp() == 0:
            print("|| Bravo ! Tu as gagné avec le pokemon " + self.pokemon1.getname() + " ||\n")
            print(" ")
            self.winner = True