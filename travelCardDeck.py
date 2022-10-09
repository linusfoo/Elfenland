# from travelCard import TravelCard, TravelCardName
from factory import Travel_Card_Factory
import random

class TravelCardDeck:

    def __init__(self, var):
        self.variant = var
        self.travel_cards = []
        self.faceup_travelCards = []
        cards = Travel_Card_Factory()
        from variant import Variant
        if self.variant == Variant.elfenland_org or self.variant == Variant.elfenland_4 or self.variant == Variant.elfenland_destination_4 or self.variant == Variant.elfenland_destination:
            for i in range(0, 10):
                self.travel_cards.append(cards.dragon)
                self.travel_cards.append(cards.unicorn)
                self.travel_cards.append(cards.troll_wagon)
                self.travel_cards.append(cards.elfcycle)
                self.travel_cards.append(cards.magic_cloud)
                self.travel_cards.append(cards.giant_pig)
                self.travel_cards.append(cards.raft)
            for i in range(0,2):
                cards = Travel_Card_Factory()
                self.travel_cards.append(cards.raft)
            random.shuffle(self.travel_cards)
    
        if self.variant == Variant.elfengold_org or self.variant == Variant.elfengold_random:
            for i in range(0, 9):
                cards = Travel_Card_Factory()
                self.travel_cards.append(cards.dragon)
                self.travel_cards.append(cards.unicorn)
                self.travel_cards.append(cards.troll_wagon)
                self.travel_cards.append(cards.elfcycle)
                self.travel_cards.append(cards.magic_cloud)
                self.travel_cards.append(cards.giant_pig)
                self.travel_cards.append(cards.raft)    
            random.shuffle(self.travel_cards)

        if self.variant == Variant.elfengold_witch or self.variant == Variant.elfengold_random_witch:
            for i in range(0, 9):
                self.travel_cards.append(cards.dragon)
                self.travel_cards.append(cards.unicorn)
                self.travel_cards.append(cards.troll_wagon)
                self.travel_cards.append(cards.elfcycle)
                self.travel_cards.append(cards.magic_cloud)
                self.travel_cards.append(cards.giant_pig)
                self.travel_cards.append(cards.raft)
            for i in range(0, 6):
                self.travel_cards.append(cards.witch)
            random.shuffle(self.travel_cards)
            for i in range(0, 3):
                c = self.travel_cards.pop()
                c.isFaceUp = True
                self.faceup_travelCards.append(c)

    def getDeck(self):
        return self.travel_cards
        
    def draw(self):
        return self.travel_cards.pop()

       

