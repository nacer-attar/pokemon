from pokemon import Pokemon
from typeeau import eau
from typenormal import normal
from typefeu import feu


class terre (Pokemon) :
    def __init__ (self, name, lvl, atkpts):
        Pokemon.__init__(self, name, lvl, atkpts)

    def afficherstats (self):
        print (f"Nom = {self.name}\n")
