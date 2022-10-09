class Path():

    def __init__(self, pTown1, pTown2, road_type, x, y):
        self.town1 = pTown1
        self.town2 = pTown2
        self.road_type = road_type
        self.transportCounter = None
        self.tcx = x
        self.tcy = y
        self.has_obstacle = False

    def getRoadType(self):
        return self.road_type

    def toString(self):
        return str(self.town1.name) + " to " + str(self.town2.name)

    def setTransportCounter(self, tc, screen, sprite):
        self.transportCounter = tc
        screen.blit(sprite, (self.tcx, self.tcy))

    def getTransportCounter(self):
        return self.transportCounter

    def clearTransportCounter(self):
        self.transportCounter = None

class WaterWay():
    def __init__(self, pTown1, pTown2, pwwtype):
        self.town1 = pTown1
        self.town2 = pTown2
        self.WaterWay_Type = pwwtype

    def getWaterWayType(self):
        return self.WaterWay_Type

    def toString(self):
        return str(self.town1.name) + " to " + str(self.town2.name)

    def getTown1(self):
        return self.town1()

    def getTown2(self):
        return self.town2()

