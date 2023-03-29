from pokemon import Pokemon
from typeeau import eau
from typeterre import terre
from typenormal import normal

class feu (Pokemon):
    def __init__ (self, name, lvl, atkpts):
        super().__init__(self, name, lvl, atkpts)

    def afficherstats (self):
        print (f"Nom = {self._name}\n")

f=feu()
print (f.afficherstats())