class Town():
    
    def __init__(self,pWidth, pHeight, pname, value):
        # super().__init__(pWidth,pHeight)
        self.width = pWidth
        self.height = pHeight
        self.name = pname
        self.points_avail = []
        self.adj = []
        self.value = value

    def remove_points(self):
        return True

    def get_name(self):
        return self.name

    def addPoints(player_list):
        return True

    def add_adj(self, ptown):
        self.adj.append(ptown)

    def get_adj(self):
        return self.adj
    
    def get_location(self):
        return [self.width, self.height]

    def isAdjacent(self, town1):
        for town in self.get_adj():
            if town1.name == town.name:
                return True
        return False

    def getX(self):
        return self.width