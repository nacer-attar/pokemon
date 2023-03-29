from pokemon import Pokemon
from typenormal import normal
from typeterre import terre
from typefeu import feu


class eau (Pokemon) :
    def __init__ (self, name, lvl, atkpts):
        Pokemon.__init__(self, name, lvl, atkpts)

    def afficherstats (self):
        print (f"Nom = {self.name}\n")
