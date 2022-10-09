import random
import copy
from transportCounter import TransportCounterName
from road_type import Road_Type
from travelCardDeck import TravelCardDeck
from transportCounterDeck import TransportCounterDeck
from variant import Variant
from factory import Transport_Card_Factory, Town_Factory, Path_Factory
from phaseName import PhaseName
import math
from player import Player








class Game():

    def __init__(self, playerList,variant):
        self.counter_factory = Transport_Card_Factory()
        self.players = playerList
        self.traveldeck = TravelCardDeck(variant)
        self.transportDeck = TransportCounterDeck(variant)
        self.avail_colours = ["red", "blue", "black", "purple", "green", "yellow"]
        self.currRound = 1
        self.currentPhase = 3
        self.numOfRounds = 3
        self.variant = variant
        self.towns = Town_Factory()
        self.currPlayerNum = 0
        self.winner = None
        self.AllPaths = Path_Factory()
        self.passed = []
        self.resetRound = False
        self.end = False
        self.lastEdit = -1
        self.isSavedGame = False

    def changeVariant(self,var):
        if var == Variant.elfenland_4:
            self.variant = Variant.elfenland_4
            self.numOfRounds = 4
        if var == Variant.elfenland_org:
            self.variant = Variant.elfenland_org
            self.numOfRounds = 3
        if var == Variant.elfenland_destination:
            self.variant = Variant.elfenland_destination
            self.numOfRounds = 3
            for i in range(0,len(self.players)):
                l = copy.deepcopy(self.towns.towns)
                dt = random.choice(l)
                while(dt.name== self.towns.ELVENHOLD.name):
                    dt = random.choice(self.towns.towns)
                self.players[i].destinationTown = dt
                l.remove(dt)
        if var == Variant.elfenland_destination_4:
            self.variant = Variant.elfenland_destination
            self.numOfRounds = 4
            for i in range(0,len(self.players)):
                l = copy.deepcopy(self.towns.towns)
                dt = random.choice(l)
                while(dt== self.towns.ELVENHOLD):
                    dt = random.choice(self.towns.towns)
                self.players[i].destinationTown = dt
                l.remove(dt)
        return self


    def valid_tc(self, rt, tc):
        print("#### Game.py, valid_tc: TC: ", tc.name, " Road Type: ", rt.value)
        if rt == Road_Type.WOOD:
            return True
        if rt == Road_Type.PLAIN:
            if tc.name == TransportCounterName.unicorn:
                return False
            else:
                return True
        elif rt == Road_Type.DESERT:
            if tc.name == TransportCounterName.giantPig or tc.name == TransportCounterName.magicCloud \
                    or tc.name == TransportCounterName.elfcycle:
                return False
            else:
                return True
        elif rt == Road_Type.MOUNTAIN:
            if tc.name == TransportCounterName.giantPig:
                return False
            else:
                return True


    def setTransportCounterOnPath(self, x, y, tc):
        pth, set = self.findPath(x, y)
        o_pth, o_set = self.findPathUnchecked(x, y)
        if set and tc.name is not TransportCounterName.obstacle:
            i = self.AllPaths.paths.index(pth)
            if self.valid_tc(pth.road_type, tc) is True:
                print("#### Game.py, setTransportCounterOnPath: Returning True.")
                pth.transportCounter = tc
                self.AllPaths.paths[i] = pth
                return set, self, 0
            else:
                print("#### Game.py, setTransportCounterOnPath: Illegal Transport Counter Exception: Returning False.")
                return False, self, -1
        elif o_set and tc.name is TransportCounterName.obstacle:
            i = self.AllPaths.paths.index(o_pth)
            if self.valid_tc(o_pth.road_type, tc) is True:
                print("#### Game.py, setObstacleOnPath: Returning True.")
                o_pth.has_obstacle = True
                self.AllPaths.paths[i] = o_pth
                return o_set, self, 0
            else:
                print("#### Game.py, setTransportCounterOnPath: Illegal Transport Counter Exception: Returning False.")
                return False, self, -1
        elif not set:
            print("#### Game.py, setTransportCounterOnPath: Returning False.")
        return set, self, 0

    def getPlayer(self, i):
        return self.players[i]

    def removePlayer(self,i):
        if i < len(self.players):
            for i in range(i,6):
                self.players.pop(len(self.players)-1)
        return self
        

    def findPath(self, x, y):
        legal = 30
        for path in self.AllPaths.paths:
            sqx = (x - 35 - path.tcx) ** 2
            sqy = (y - 35- path.tcy) ** 2
            if math.sqrt(sqx + sqy) < legal and path.transportCounter is None:  # Check if path is already placed with a transport counter,
                print("#### Game.py, findPath: Returning True.")
                return path, True
        print("Path is not correct or has an existing counter.")
        print("#### findPath: Returning False.")
        return None, False

    def findPathUnchecked(self, x, y):
        legal = 30
        for path in self.AllPaths.paths:
            sqx = (x  -35 - path.tcx) ** 2
            sqy = (y - 35 -path.tcy) ** 2
            if math.sqrt(sqx + sqy) < legal:
                print("#### Game.py, findPath: Returning True.")
                return path, True
        print("Path is not correct or has an existing counter.")
        print("#### findPath: Returning False.")
        return None, False

    def update(self,p1):
        self.players[p1.player_num] = p1
        return self

    def getDistance(self, player):
        start = player.town
        dest = player.destinationTown
        towns = self.towns.getTowns()
        visited = {v: False for v in towns}
        queue = []
        queue.append(start)
        visited[start] = True
        counter = 0

        while queue:
            s = queue.pop(0)
            counter += 1
            for t in s.adj:
                for town in towns:
                    if town.name == t.name:
                        if not visited[town]:
                            queue.append(town)
                            visited[town] = True
                            if t.name == dest.name:
                                queue.clear()
                                break

        return counter
    

    def endGame(self):
        print("game ended")
        if self.variant == Variant.elfenland_4:
            for player in self.players:
                if len(player.points) == 0:
                    if self.winner == None:
                        self.winner = player
                    else: 
                        if len(self.winner.travel_cards) > len(player.travel_cards):
                            self.winner = player
            if self.currRound == 4 : # and last phase and last player
                if self.winner == None: #no one got all the towns yet
                    minPoints = 0
                    for player in self.players:
                        if (20 - len(player.points)) > minPoints:
                            self.winner = player
                            minPoints = (20-len(player.points))
                        elif (20 - len(player.points))== minPoints:
                            if self.winner != None:
                                self.winner = player
                            else:
                                if len(self.winner.travel_cards) > len(player.travel_cards):
                                    self.winner = player
                            
        if self.variant == Variant.elfenland_org:
            if self.currRound == 3 : # and last phase and last player
                if self.winner == None: #no one got all the towns yet
                    minPoints = 0
                    for player in self.players:
                        if (20 - len(player.points)) > minPoints:
                            self.winner = player
                            minPoints = (20-len(player.points))
                        elif (20 - len(player.points))== minPoints:
                            if self.winner != None:
                                self.winner = player
                            else:
                                if len(self.winner.travel_cards) > len(player.travel_cards):
                                    self.winner = player

        if self.variant == Variant.elfenland_destination:
            if self.currRound == 3 : # and last phase and last player
                minPoints = -10000
                for player in self.players:
                    if (20 - len(player.points) - self.getDistance(player)) > minPoints:
                        self.winner = player
                        minPoints = (20 - len(player.points) - self.getDistance(player))
                    elif (20 - len(player.points) - self.getDistance(player))== minPoints:
                        if self.winner != None:
                            self.winner = player
                        else:
                            if len(self.winner.travel_cards) > len(player.travel_cards):
                                self.winner = player
        self.end = True
        for p in self.players:
            p.command = None
        return self
    def copyData(self,g1):
        self.players = g1.players
        for i in range(0, len(self.players)):
            if self.players[i].colour == ' ':
                self.players[i].colour = g1.players[i].colour
        # if len(g1.traveldeck) < len(self.traveldeck):
        self.traveldeck = g1.traveldeck
        # if len(g1.transportDeck) < len(self.transportDeck):
        self.transportDeck = g1.transportDeck
        self.avail_colours = g1.avail_colours
        self.currRound = g1.currRound
        self.currentPhase = g1.currentPhase
        self.numOfRounds = g1.numOfRounds
        self.variant = g1.variant
        self.towns = g1.towns
        self.currPlayerNum = g1.currPlayerNum
        self.winner = g1.winner
        self.AllPaths = g1.AllPaths

    def dsitributeResources(self):
        for player in self.players:
            player.inGame(self)
            obstacle = self.counter_factory.obstacle
            obstacle.changeFace = True
            player.transport_cards.append(obstacle)
            for i in range(0,8):
                player.travel_cards.append(self.traveldeck.draw)
        self.currentPhase = PhaseName.DrawFaceUpCounterOne

    def cleanMap(self):
        for path in self.AllPaths.paths:
            path.transportCounter = None
