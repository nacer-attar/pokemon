import random
from monstredepoche import *

class stats (Pokemon):

    def __init__(self) :
        super().__init__()

    def setstats (self):
        if self.getname() == "Bulbizarre":
            self.sethp(random.randint(43,48))
            self.attack = random.randint(55,60)
            self.defense = random.randint(25,30)
            self.lvl = random.randint(5,15)

        elif self.getname() == "Carapuce":  
            self.sethp(random.randint(42,47))
            self.attack = random.randint(47,52)
            self.defense = random.randint(31,36)
            self.lvl = random.randint(5,15)
        
        elif self.getname() == "Salamèche":
            self.sethp(random.randint(42,48))
            self.attack = random.randint(54,59)
            self.defense = random.randint(21,26)
            self.lvl = random.randint(5,15)
        
        elif self.getname() == "Evoli":
            self.sethp(random.randint(37,42))
            self.attack = random.randint(48,53)
            self.defense = random.randint(28,33)
            self.lvl = random.randint(5,15)


        
    def displayPokemon(self):
        print(self.getname() + '\nPoints de vie: ' + str(self.gethp()) + "\nAttaque: " + str(self.attack) + "\nDéfense: " + str(self.defense))