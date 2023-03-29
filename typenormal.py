from pokemon import Pokemon
from typeeau import eau
from typeterre import terre
from typefeu import feu


class normal (Pokemon) :
    def __init__ (self, name, lvl, atkpts):
        Pokemon.__init__(self, name, lvl, atkpts)

    def afficherstats (self):
        print (f"Nom = {self.name}\n")
