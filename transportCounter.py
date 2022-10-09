from enum import Enum , auto

class TransportCounter():
    def __init__(self, name):
        self.name = name
        self.isFaceUp = False
    
    def changeFace(self, is_facing_up):
        self.isFaceUp = is_facing_up

class TransportCounterName(Enum):
    giantPig = auto()
    magicCloud = auto()
    elfcycle = auto()
    unicorn = auto()
    trollWagon = auto()
    dragon = auto()
    treeTrunk = auto()
    obstacle = auto()
    goldpiece = auto()
    seaMonsterObstacle = auto()
    double = auto()
    exchange = auto()


    


