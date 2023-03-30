from pokemon import Pokemon

class fire (Pokemon) :
    def __init__(self, name, lvl, atkpts, type) -> None:
        super().__init__(self, name, lvl, atkpts, type)
        
    def checktypefire(self) :  #vérifie si le mdp existe dans le json en comparant le hash du mdp du user avec les hashes enregistrés.
        with open("typefeu.json", "r") as file:
            if self._name + "\n" in file:
                self._hp = 69
                self.atkpts = 83
                self.defpts = 69
                self.type = 'fire'

    def weakness (self):
        pass
    