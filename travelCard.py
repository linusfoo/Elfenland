from enum import Enum , auto

class TravelCard():
    def __init__(self, name):
        self.name = name
        self.isFaceUp = False

    def changeFace(self, is_facing_up):
        self.isFaceUp = is_facing_up


class TravelCardName(Enum):
    giantPig = auto()
    magicCloud = auto()
    elfcycle = auto()
    unicorn = auto()
    trollWagon = auto()
    dragon = auto()
    raft = auto()
    witch = auto()
    goldCard = auto()
