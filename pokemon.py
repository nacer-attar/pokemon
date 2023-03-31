import random

class Pokemon:
    def __init__ (self):
        self.__name = " "
        self.__hp = 50
        self.lvl = 1
        self.attack = 10
        self.defense = 0
        self.type = []
        self.pokedex = [["Bulbizarre",["Plante"]],
                        ["Salamèche", ["Feu"]],
                        ["Carapuce",  ["Eau"]],
                        ["Evoli",     ["Normal"]]]
    
    def setname (self, name):
        self.__name = name
    def getname (self):
        return self.__name

    def sethp (self, hp):
        self.__hp = hp
    def gethp (self):
        return self.__hp

    def setlvl (self, lvl):
        self.lvl = lvl
    def getlvl (self):
        return self.lvl
    
    def setattack (self, attack):
        self.attack = attack
    def getattack (self):
        return self.attack
    
    def setdefense (self, defense):
        self.defense = defense
    def getdefense (self):
        return self.defense

    def playerpokemon (self):
        choice = False
        for pokemon in self.pokedex:
            pokelist = ' et '.join (str(i) for i in pokemon[1]) #on transforme la list de type en str
            print (pokemon[0], "de type ", pokelist ) #print de la liste de pokemon
        while not choice :
            pokechoice = input ("Choisi un Pokemon depuis la liste : ")
            for name, type in self.pokedex:
                if name == pokechoice:
                        self.setname(pokechoice)
                        self.type = type
                        choice = True
                        break
                else :
                    print ("Si je mets plus de Pokemon on va me faire un procés...")
    
    def pokerandom(self):
        random_pokemon = random.choice(self.pokedex)
        self.setname = random_pokemon[0]
        self.type = random_pokemon[1]