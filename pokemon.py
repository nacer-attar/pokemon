class Pokemon:
    def __init__ (self, name, lvl, atkpts, type):
        self._name = name
        self._hp = 100
        self.lvl = lvl
        self.atkpts = atkpts
        self.defpts = 0
        self.type = type

    #set n get hp
    def sethp (self, hp):
        self._hp = hp

    def gethp (self):
        return self._hp
    #set n get defpts
    def setdefpts (self,defpts):
        self.defpts = defpts

    def getdefpts (self):
        return self.defpts
    