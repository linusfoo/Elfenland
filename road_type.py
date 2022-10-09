from enum import Enum, auto

class Road_Type(Enum):
    WOOD = auto()
    PLAIN = auto()
    DESERT = auto()
    MOUNTAIN = auto()

class WaterWay_Type(Enum):
    DOWNSTREAM = auto()
    UPSTREAM = auto()
    LAKE = auto()
