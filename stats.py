import random
from pokemon.pokemon import *

class stats (Pokemon):

    def __init__(self) :
        super().__init__()

    def setstats (self):
        if self.__name == "Bulbizarre":
            self.__hp = random.randint(43,48)
            self.attack = random.randint(55,60)
            self.defense = random.randint(55,60)
            self.lvl = random.randint(5,15)

        elif self.__name == "Carapuce":  
            self.__hp = random.randint(42,47)
            self.attack = random.randint(47,52)
            self.defense = random.randint(63,68)
            self.lvl = random.randint(5,15)
        
        elif self.__name == "Salamèche":
            self.__hp = random.randint(42,48)
            self.attack = random.randint(54,59)
            self.defense = random.randint(45,50)
            self.lvl = random.randint(5,15)
        
        elif self.__name == "Evoli":
            self.__hp = random.randint(37,42)
            self.attack = random.randint(48,53)
            self.defense = random.randint(56,61)
            self.lvl = random.randint(5,15)


        
