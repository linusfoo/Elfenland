from enum import Enum , auto


class PhaseName(Enum):
    DrawTravelCards = auto()
    DrawHiddenCounter = auto()
    DrawFaceUpCounterOne = auto()
    DrawFaceUpCounterTwo = auto()
    DrawFaceUpCounterThree = auto()
    Auction = auto()
    PlanTravel = auto()
    FinishRound = auto()

    magicCloud = auto()
    elfcycle = auto()
    unicorn = auto()
    trollWagon = auto()
    dragon = auto()
    raft = auto()
    witch = auto()
    goldCard = auto()