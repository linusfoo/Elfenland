import os

import tkinter

# import pyautogui as pyautogui

from transportCounter import TransportCounterName
from travelCard import TravelCardName, TravelCard
from road_type import Road_Type, WaterWay_Type
from factory import Town_Factory, Path_Factory, WaterWay_Factory
import pygame
import os
from point import Point
import math

# import pyautogui


# prompt = tkinter.Tk()
# prompt.geometry("300x200")

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
# AllPaths = Path_Factory()
TOWN_FACTORY = Town_Factory()
AllWaterWays = WaterWay_Factory()
ELVENHOLD = TOWN_FACTORY.ELVENHOLD
LAPPHALYA = TOWN_FACTORY.LAPPHALYA
DAGAMURA = TOWN_FACTORY.DAGAMURA
VIRST = TOWN_FACTORY.VIRST
JXARA = TOWN_FACTORY.JXARA
BEATA = TOWN_FACTORY.BEATA
STRYKHAVEN = TOWN_FACTORY.STRYKHAVEN
ERGEREN = TOWN_FACTORY.ERGEREN
RIVINIA = TOWN_FACTORY.RIVINIA
TICHIH = TOWN_FACTORY.TICHIH
THROTMANNI = TOWN_FACTORY.THROTMANNI

PARUNDIA = TOWN_FACTORY.PARUNDIA
LISSELEN = TOWN_FACTORY.USSELEN
WYLHIEN = TOWN_FACTORY.WYLHIEN
KIHROMAH = TOWN_FACTORY.KIHROMAH
YTTAR = TOWN_FACTORY.YTTAR
FEODOR = TOWN_FACTORY.FEODOR
MAHDAVIKIA = TOWN_FACTORY.MAHDAVIKIA
JACCARANDA = TOWN_FACTORY.JACCARANDA
ALBARAN = TOWN_FACTORY.ALBARAN
GRANGOR = TOWN_FACTORY.GRANGOR

LAPPHALYA_POINTS = Point(LAPPHALYA, "red")
DAGAMURA_POINTS = Point(DAGAMURA, "red")
VIRST_POINTS = Point(VIRST, "red")
JXARA_POINTS = Point(JXARA, "red")
BEATA_POINTS = Point(BEATA, "red")
STRYKHAVEN_POINTS = Point(STRYKHAVEN, "red")
ERGEREN_POINTS = Point(ERGEREN, "red")
RIVINIA_POINTS = Point(RIVINIA, "red")
TICHIH_POINTS = Point(TICHIH, "red")
THROTMANNI_POINTS = Point(THROTMANNI, "red")
PARUNDIA_POINTS = Point(PARUNDIA, "red")
LISSELEN_POINTS = Point(LISSELEN, "red")
WYLHIEN_POINTS = Point(WYLHIEN, "red")
KIHROMAH_POINTS = Point(KIHROMAH, "red")
YTTAR_POINTS = Point(YTTAR, "red")
FEODOR_POINTS = Point(FEODOR, "red")
MAHDAVIKIA_POINTS = Point(MAHDAVIKIA, "red")
JACCARANDA_POINTS = Point(JACCARANDA, "red")
ALBARAN_POINTS = Point(ALBARAN, "red")
GRANGOR_POINTS = Point(GRANGOR, "red")

LAPPHALYA_POINTS_GREEN = Point(LAPPHALYA, "green")
DAGAMURA_POINTS_GREEN = Point(DAGAMURA, "green")
VIRST_POINTS_GREEN = Point(VIRST, "green")
JXARA_POINTS_GREEN = Point(JXARA, "green")
BEATA_POINTS_GREEN = Point(BEATA, "green")
STRYKHAVEN_POINTS_GREEN = Point(STRYKHAVEN, "green")
ERGEREN_POINTS_GREEN = Point(ERGEREN, "green")
RIVINIA_POINTS_GREEN = Point(RIVINIA, "green")
TICHIH_POINTS_GREEN = Point(TICHIH, "green")
THROTMANNI_POINTS_GREEN = Point(THROTMANNI, "green")
PARUNDIA_POINTS_GREEN = Point(PARUNDIA, "green")
LISSELEN_POINTS_GREEN = Point(LISSELEN, "green")
WYLHIEN_POINTS_GREEN = Point(WYLHIEN, "green")
KIHROMAH_POINTS_GREEN = Point(KIHROMAH, "green")
YTTAR_POINTS_GREEN = Point(YTTAR, "green")
FEODOR_POINTS_GREEN = Point(FEODOR, "green")
MAHDAVIKIA_POINTS_GREEN = Point(MAHDAVIKIA, "green")
JACCARANDA_POINTS_GREEN = Point(JACCARANDA, "green")
ALBARAN_POINTS_GREEN = Point(ALBARAN, "green")
GRANGOR_POINTS_GREEN = Point(GRANGOR, "green")


class Player():

    def __init__(self, pPlayer_Num, colour, town):

        self.player_num = pPlayer_Num
        self.colour = colour
        self.town = town
        self.ready = False
        self.hasWon = False
        self.transport_cards = []
        self.travel_cards = []
        self.obstacle_counter = None
        self.name = " "
        self.phase_num = 0
        self.passed = False
        self.clicked = [0, 0]
        self.command = None
        self.Turn = 0
        self.isTurn = True
        self.inGame = None
        self.destinationTown = ELVENHOLD
        self.chosenTCidxForPhase4 = None
        self.passed = False
        self.dest = None
        self.message_box = None
        self.pathDuringChoice = None
        self.tried_moving = False
        self.choosing_caravan_cards = False
        self.choosing_caravan_town = False
        self.selected_caravan_cards = []
        self.count = 0
        self.caravan_town = None
        # self.roundNum = 1

        if colour == "red":
            self.points = [TICHIH_POINTS, LAPPHALYA_POINTS, DAGAMURA_POINTS,
                           VIRST_POINTS, JXARA_POINTS, BEATA_POINTS, STRYKHAVEN_POINTS,
                           ERGEREN_POINTS, RIVINIA_POINTS, THROTMANNI_POINTS, PARUNDIA_POINTS,
                           LISSELEN_POINTS, WYLHIEN_POINTS, KIHROMAH_POINTS, YTTAR_POINTS, FEODOR_POINTS,
                           MAHDAVIKIA_POINTS, JACCARANDA_POINTS, ALBARAN_POINTS, GRANGOR_POINTS]
            # self.rect = (self.town.width+10,self.town.height+10,10,30)
        else:
            self.points = [TICHIH_POINTS_GREEN, LAPPHALYA_POINTS_GREEN, DAGAMURA_POINTS_GREEN,
                           VIRST_POINTS_GREEN, JXARA_POINTS_GREEN, BEATA_POINTS_GREEN, STRYKHAVEN_POINTS_GREEN,
                           ERGEREN_POINTS_GREEN, RIVINIA_POINTS_GREEN, THROTMANNI_POINTS_GREEN, PARUNDIA_POINTS_GREEN,
                           LISSELEN_POINTS_GREEN, WYLHIEN_POINTS_GREEN, KIHROMAH_POINTS_GREEN, YTTAR_POINTS_GREEN,
                           FEODOR_POINTS_GREEN,
                           MAHDAVIKIA_POINTS_GREEN, JACCARANDA_POINTS_GREEN, ALBARAN_POINTS_GREEN, GRANGOR_POINTS_GREEN]
            # self.rect = (self.town.width,self.town.height,10,30)

        self.pointNum = len(self.points)

        # resources

    # def getpoints(self):
    #     return len(self.points)

    def clickedTown(self, x, y, dest):
        org_dest = dest
        sqx = (x - LAPPHALYA.width) ** 2
        sqy = (y - LAPPHALYA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = LAPPHALYA
            return move, dest
        sqx = (x - DAGAMURA.width) ** 2
        sqy = (y - DAGAMURA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = DAGAMURA
            return move, dest
        sqx = (x - VIRST.width) ** 2
        sqy = (y - VIRST.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = VIRST
            return move, dest
        sqx = (x - JXARA.width) ** 2
        sqy = (y - JXARA.height) ** 2

        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = JXARA
            return move, dest
        sqx = (x - ELVENHOLD.width) ** 2
        sqy = (y - ELVENHOLD.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = ELVENHOLD
            return move, dest
        sqx = (x - STRYKHAVEN.width) ** 2
        sqy = (y - STRYKHAVEN.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = STRYKHAVEN
            return move, dest
        sqx = (x - BEATA.width) ** 2
        sqy = (y - BEATA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = BEATA
            return move, dest
        sqx = (x - ERGEREN.width) ** 2
        sqy = (y - ERGEREN.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = ERGEREN
            return move, dest
        sqx = (x - RIVINIA.width) ** 2
        sqy = (y - RIVINIA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = RIVINIA
            return move, dest
        sqx = (x - THROTMANNI.width) ** 2
        sqy = (y - THROTMANNI.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = THROTMANNI
            return move, dest
        sqx = (x - TICHIH.width) ** 2
        sqy = (y - TICHIH.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = TICHIH
            return move, dest

        sqx = (x - PARUNDIA.width) ** 2
        sqy = (y - PARUNDIA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = PARUNDIA
            return move, dest
        sqx = (x - LISSELEN.width) ** 2
        sqy = (y - LISSELEN.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = LISSELEN
            return move, dest
        sqx = (x - WYLHIEN.width) ** 2
        sqy = (y - WYLHIEN.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = WYLHIEN
            return move, dest
        sqx = (x - KIHROMAH.width) ** 2
        sqy = (y - KIHROMAH.height) ** 2

        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = KIHROMAH
            return move, dest
        sqx = (x - YTTAR.width) ** 2
        sqy = (y - YTTAR.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = YTTAR
            return move, dest
        sqx = (x - FEODOR.width) ** 2
        sqy = (y - FEODOR.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = FEODOR
            return move, dest
        sqx = (x - MAHDAVIKIA.width) ** 2
        sqy = (y - MAHDAVIKIA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = MAHDAVIKIA
            return move, dest
        sqx = (x - JACCARANDA.width) ** 2
        sqy = (y - JACCARANDA.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = JACCARANDA
            return move, dest
        sqx = (x - ALBARAN.width) ** 2
        sqy = (y - ALBARAN.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = ALBARAN
            return move, dest
        sqx = (x - GRANGOR.width) ** 2
        sqy = (y - GRANGOR.height) ** 2
        if math.sqrt(sqx + sqy) < 60:
            move = True
            dest = GRANGOR
            return move, dest
        if dest == org_dest:
            return False, dest

    def promptPathSelection(self):
        global prompt
        prompt = tkinter.Tk()
        prompt.geometry("500x350")
        prompt.title("Account Login")
        tkinter.Label(text="Please Select the type of Path", bg="yellow", width="300", height="2",
                      font=("Calibri", 16)).pack()
        tkinter.Label(text="").pack()
        ret = tkinter.Button(text="Ground", height="3", width="30", command=self.isGround).pack()
        tkinter.Label(text="").pack()
        ret = tkinter.Button(text="Water", height="3", width="30", command=self.isNotGround).pack()
        return ret

    def isGround(self):
        prompt.destroy()
        return True

    def isNotGround(self):
        prompt.destroy()
        return False

    def numberOfTCardsRequired(self, tc, rt):

        if rt == Road_Type.PLAIN:
            if tc.name == TransportCounterName.giantPig or tc.name == TransportCounterName.elfcycle \
                    or tc.name == TransportCounterName.trollWagon or tc.name == TransportCounterName.dragon:
                return 1
            elif tc.name == TransportCounterName.magicCloud:
                return 2
            else:
                return -1

        elif rt == Road_Type.WOOD:
            if tc.name == TransportCounterName.giantPig or tc.name == TransportCounterName.elfcycle \
                    or tc.name == TransportCounterName.unicorn:
                return 1
            elif tc.name == TransportCounterName.magicCloud or tc.name == TransportCounterName.trollWagon \
                    or tc.name == TransportCounterName.dragon:
                return 2
            else:
                return -1

        elif rt == Road_Type.DESERT:
            if tc.name == TransportCounterName.dragon:
                return 1
            elif tc.name == TransportCounterName.unicorn or tc.name == TransportCounterName.trollWagon:
                return 2
            else:
                return -1

        elif rt == Road_Type.MOUNTAIN:
            if tc.name == TransportCounterName.magicCloud or tc.name == TransportCounterName.unicorn \
                    or tc.name == TransportCounterName.dragon:
                return 1
            elif tc.name == TransportCounterName.elfcycle or tc.name == TransportCounterName.trollWagon:
                return 2
            else:
                return -1

        else:
            return 0

    def checkAvailibility(self, name):
        avb = 0
        for card in self.travel_cards:
            if name.name == card.name.name:
                avb += 1
        return avb

    def canMoveRoad(self, p):   # Checking the legality of the road movement on the chosen path.
        rt = p.road_type    # We retrieve the road type.
        if p.transportCounter is None:  # If there is *no* transport counter set on the road, we return False.
            return False, -1, " "
        else:
            num = self.numberOfTCardsRequired(p.transportCounter, rt)  # We check the number of cards that will be required to move given the road type and transport counter.
            if num != -1 and p.has_obstacle:  # Check if the path has an obstacle.
                num += 1        # Add 1 extra required travel card.
            print("Number of travel cards required: ", num)
            nam = p.transportCounter.name    # We get the name of the type of card we need.
            avb = self.checkAvailibility(nam)     # Check how many Travel Cards the player has for the specified type.
            if num == -1 or num > avb:  # If the transport counter type placed doesn't allow for movement with the road type.
                return False, -1, " "    # We return the move as illegal.
            else:
                return True, num, nam  # If the everything is good, we

    def canMoveWater(self, w):
        wt = w.WaterWay_Type
        num = 0

        if wt is WaterWay_Type.LAKE or wt is WaterWay_Type.UPSTREAM:
            num += 2
        else:
            num += 1

        avb = 0
        for card in self.travel_cards:
            if card.name is TravelCardName.raft:
                avb += 1

        if num > avb:
            return False, -1
        else:
            return True, num

    def getPath(self, currTown, desTown, game):
        for path in game.AllPaths.paths:
            if (path.town1.name == currTown.name and path.town2.name == desTown.name) or (
                    path.town1.name == desTown.name and path.town2.name == currTown.name):
                return path
            else:
                # print(path.toString())
                continue
        print("Didn't find any land route")
        return None

    def getWaterWay(self, currTown, desTown):
        for way in AllWaterWays.water_ways:
            if way.town1.name == currTown.name and way.town2.name == desTown.name:
                return way
            else:
                # print(way.toString())
                continue
        print("Didn't find any water route")
        return None

    def move(self, x, y, game):
        self.tried_moving = True
        road_options = []   # list of road options
        water_options = []  # list of water options
        moveOnGround = False    # set movement legality on ground as false
        moveOnWater = False     # set movement legality on ground as false
        move, dest = self.clickedTown(x, y, self.town)  # Get the name of the destination town
        print("CurrTown is ", self.town.name, " DestTown is ", dest.name)
        p = self.getPath(self.town, dest, game)     # Check if a ground path exists from current town to destination town.
        if p is None:       # If *no* ground path exists, we pass and check if a water route existis.
            pass
        else:
            road_options.append(p)  # If there is a ground path we append to the list of road options.
            print("CurrPath land is ", p.toString())
        w = self.getWaterWay(self.town, dest)  # Check if a water route exists from current town to destination town.
        if w is None:   # If *no* water path exists, we pass.
            pass
        else:
            water_options.append(w) # Other wise append to the list of water options.
            print("CurrPath water is ", w.toString())
        number = len(road_options) + len(water_options) # We check what the total number of options are.
        num = 0     # Number of travel cards required are set to 0.
        nam = ""    # The name of the travel card is set to an empty String.
        print("Number of ways to travel: ", number)
        if number > 1:      # If there's more than 1 option
            print("###player.py, Click on either the Land or Water button.")
            self.message_box = "Two paths available. Click on either the \"Land\" or \"Water\" button to select."
            self.pathDuringChoice = [p, w]
            self.dest = dest
            print("###player.py, Click on either the Land or Water button. Path during choice length: ", str(len(self.pathDuringChoice)))
            return True, 2
        elif number == 1 and self.town.isAdjacent(dest):
            if len(road_options) == 1:
                print("Figuring out if it can move on land:")
                moveOnGround, num, nam = self.canMoveRoad(p)
            else:
                print("Figuring out if it can move on water:")
                moveOnWater, num = self.canMoveWater(w)

        moved = move and (moveOnGround or moveOnWater)
        if moved:
            self.town = dest
            for point in self.points:
                if point.town.name == dest.name:
                    self.points.remove(point)
            self.update()
            if moveOnWater:
                self.message_box = "Click on a town to move to"
                deleted = 0
                for tCard in self.travel_cards:
                    if tCard.name == TravelCardName.raft and num > deleted:
                        self.travel_cards.remove(tCard)
                        deleted += 1
                    else:
                        continue
            elif moveOnGround:
                self.message_box = "Click on a town to move to"
                deleted = 0
                for tCard in self.travel_cards:
                    if tCard.name.name == nam.name and num > deleted:
                        self.travel_cards.remove(tCard)
                        deleted += 1
                    else:
                        continue
        # else:
        #     self.message_box = "Didn't move. Try selecting another route."
        return moved, 0


    def set_caravan_town(self, x, y, game):
        move, dest = self.clickedTown(x, y, self.town)  # Get the name of the destination town
        print("#player.py, #479 CurrTown is ", self.town.name, " DestTown is ", dest.name)
        if move and self.town.isAdjacent(dest):
            self.caravan_town = dest
            p = self.getPath(self.town, dest, game)
            obs = p.has_obstacle
            if obs and len(self.travel_cards) < 4:
                return False, obs
            else:
                return move, obs
        else:
            return move, False



    def move_caravan(self):
        # road_options = []  # list of road options
        # water_options = []  # list of water options
        # move, dest = self.clickedTown(x, y, self.town)  # Get the name of the destination town
        # print("CurrTown is ", self.town.name, " DestTown is ", self.caravan_town.name)
        # p = self.getPath(self.town, dest, game)  # Check if a ground path exists from current town to destination town.

        # moveOnGround = False
        # moveOnWater = False

        # if p is None:  # If *no* ground path exists, we pass and check if a water route existis.
        #     pass
        # else:
        #     road_options.append(p)  # If there is a ground path we append to the list of road options.
        #     print("CurrPath land is ", p.toString())
        #     moveOnGround, num, nam = self.canMoveRoad(p)
        # w = self.getWaterWay(self.town, dest)  # Check if a water route exists from current town to destination town.
        # if w is None:  # If *no* water path exists, we pass.
        #     pass
        # else:
        #     water_options.append(w)  # Other wise append to the list of water options.
        #     print("CurrPath water is ", w.toString())
        #     moveOnWater, num = self.canMoveWater(w)

        # number = len(road_options)  #  +  len(water_options)  # We check what the total number of options are.

        # if number > 0 and self.town.isAdjacent(dest) and self.town is not dest and moveOnGround:
        # moved = True
        self.town = self.caravan_town
        for point in self.points:
            if point.town.name == self.caravan_town.name:
                self.points.remove(point)
        self.selected_caravan_cards.clear()
        self.caravan_town = None
        self.update()
        return True, 0
        # else:
        #     moved = False
        #     self.message_box = "Select a/another route.."
        #     self.travel_cards.append(self.selected_caravan_cards)
        #     self.selected_caravan_cards.clear()
        #     return moved, -1

    def moveOnRoad(self, path):   #  Implement movement on road when Land button is selected.
        moveOnGround, num, nam = self.canMoveRoad(path)
        if moveOnGround:
            self.town = self.dest
            for point in self.points:
                if point.town.name == self.dest.name:
                    self.points.remove(point)
            self.update()
            deleted = 0
            for tCard in self.travel_cards:
                if tCard.name.name == nam.name and num > deleted:
                    self.travel_cards.remove(tCard)
                    deleted += 1
        return moveOnGround, self

    def moveOnWater(self,  path):   #  Implement movement on road when Land button is selected.
        moveOnWater, num = self.canMoveWater(path)
        if moveOnWater:
            self.town = self.dest
            for point in self.points:
                if point.town.name == self.dest.name:
                    self.points.remove(point)
            self.update()
            deleted = 0
            for tCard in self.travel_cards:
                if tCard.name == TravelCardName.raft and num > deleted:
                    self.travel_cards.remove(tCard)
                    deleted += 1
        return moveOnWater, self



    def update(self):
        self.pointNum = len(self.points)

    def drawRandomCounter(self, tcDeck):
        from phaseName import PhaseName
        self.transport_cards.append(tcDeck.draw_faceDown())
        if self.inGame.currentPhase == PhaseName.DrawFaceUpCounterOne:
            self.inGame.currentPhase = PhaseName.DrawFaceUpCounterTwo
        elif self.inGame.currentPhase == PhaseName.DrawFaceUpCounterTwo:
            self.inGame.currentPhase = PhaseName.DrawFaceUpCounterThree
        elif self.inGame.currentPhase == PhaseName.DrawFaceUpCounterThree:
            self.inGame.currentPhase = PhaseName.PlanTravel


    def clickedLand(self):
        print("#542##player.py, checking if clickedLand is true.")
        x = self.clicked[0]
        y = self.clicked[1]
        print(self.clicked[0], ", ", self.clicked[1])
        sqx = (x - 1392) ** 2
        sqy = (y - 321) ** 2
        if math.sqrt(sqx + sqy) < 30:
            return True
        else:
            return False

    def clickedWater(self):
        x = self.clicked[0]
        y = self.clicked[1]
        sqx = (x - 1392) ** 2
        sqy = (y - 425) ** 2
        if math.sqrt(sqx + sqy) < 30:
            return True
        else:
            return False

    def clickedPass(self):
        x = self.clicked[0]
        y = self.clicked[1]
        sqx = (x - 999) ** 2
        sqy = (y - 373) ** 2
        if math.sqrt(sqx + sqy) < 65:
            return True
        else:
            return False

    def clickedBasic(self):
        x = self.clicked[0]
        y = self.clicked[1]
        sqx = (x - 1382) ** 2
        sqy = (y - 694) ** 2

        radius = 30

        if math.sqrt(sqx + sqy) < radius:
            self.message_box = "Chose Basic movement."
            print("Chose Basic movement.")
            return True
        else:
            return False

    def clickedCaravan(self):
        x = self.clicked[0]
        y = self.clicked[1]
        sqx = (x - 1382) ** 2
        sqy = (y - 783) ** 2

        radius = 30

        if math.sqrt(sqx + sqy) < radius:
            self.message_box = "Chose Caravan movement."
            print("Chose Caravan movement.")
            return True
        else:
            return False

    def refreshClick(self):
        self.clicked = [0, 0]