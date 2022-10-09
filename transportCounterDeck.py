# from travelCard import TravelCard, TravelCardName
from factory import Transport_Card_Factory
import random

class TransportCounterDeck:


    def __init__(self, var):
        self.variant = var
        self.facedown_cards = []
        self.faceup_cards = []
        self.obs_cards = []
        self.cards = Transport_Card_Factory()

        from variant import Variant
        if self.variant == Variant.elfenland_org or self.variant == Variant.elfenland_4 or self.variant == Variant.elfenland_destination_4 or self.variant == Variant.elfenland_destination:
            for i in range(0, 8):
                self.facedown_cards.append(self.cards.dragon)
                self.facedown_cards.append(self.cards.unicorn)
                self.facedown_cards.append(self.cards.troll_wagon)
                self.facedown_cards.append(self.cards.elfcycle)
                self.facedown_cards.append(self.cards.magic_cloud)
                self.facedown_cards.append(self.cards.giant_pig)
            random.shuffle(self.facedown_cards)
            for i in range(0, 5):
                c = self.facedown_cards.pop()
                c.isFaceUp = True
                self.faceup_cards.append(c)

            for i in range(0, 6):
                self.obs_cards.append(self.cards.obstacle)

        if self.variant == Variant.elfengold_org:
            cards = Transport_Card_Factory()
            for _ in range(0, 4):
                self.facedown_cards.append(cards.dragon)
                self.facedown_cards.append(cards.magic_cloud)
            for _ in range(0,5):
                self.facedown_cards.append(cards.unicorn)
            for _ in range(0,8):
                self.facedown_cards.append(cards.troll_wagon)
                self.facedown_cards.append(cards.elfcycle)
            for _ in range(0,9):
                self.facedown_cards.append(cards.giant_pig)
            for _ in range(0,2):
                self.facedown_cards.append(cards.goldpiece)
                self.facedown_cards.append(cards.double)
                self.facedown_cards.append(cards.exchange)
                self.facedown_cards.append(cards.seaMonsterObstacle)
                self.facedown_cards.append(cards.obstacle)
            random.shuffle(self.facedown_cards)



    def draw_obstacle(self):
        return self.obs_cards.pop()
        
    def draw_faceDown(self):
        return self.facedown_cards.pop()

    def draw_faceUp(self, index):
        ret = self.peekFUP(index)
        self.faceup_cards.pop(index)
        card = self.facedown_cards.pop()
        card.isFaceUp = True
        self.faceup_cards.insert(index, card)
        return ret

    def peekFUP(self, index):
        return self.faceup_cards[index]
    
    # def updateDeck(self):
    #     for card in self.facedown_cards:
    #         if card.isFaceUp == True:
    #             self.faceup_cards.append(self.facedown_cards.remove(card))


       

