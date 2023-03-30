from pokemon import Pokemon

class combat (Pokemon) :
    def __init__(self, name, lvl, atkpts, pokemon1, pokemon2) -> None:
        super().__init__(self, name, lvl, atkpts)
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def checkhp (self, perdant):
        if self._hp < 0:
            return perdant
        
    def damagetable(self, atktype, deftype):
        tableau = {
            "Eau": {"Eau": 1, "Feu": 2, "Terre": 0.5, "Normal": 1},
            "Feu": {"Eau": 0.5, "Feu": 1, "Terre": 2, "Normal": 1},
            "Terre": {"Eau": 2, "Feu": 0.5, "Terre": 1, "Normal": 1},
            "Normal": {"Eau": 0.75, "Feu": 0.75, "Terre": 0.75, "Normal": 1}
        }

        indice = tableau [atktype] [deftype]
        return indice
    
    def removehp(self): 

