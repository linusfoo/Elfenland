import math
import pickle

from variant import Variant


class changeColourCommand():
    def __init__(self, player, colour, variant, numPlayers, username):
        self.player = player
        self.colour = colour
        self.variant = variant
        self.numPlayers = numPlayers
        self.username = username

    def execute(self):
        self.player.colour = self.colour
        self.player.command = None
        self.player.ready = True
        self.player.name = self.username
        return self.player, self.variant, self.numPlayers


class reSetUpCommand():
    def __init__(self, username):
        self.username = username

    def execute(self,game): 
        for player in game.players:
            if player.name == self.username:
                return player


class resetRoundCommand():
    def __init__(self, player):
        self.player = player

    def execute(self, GAME):
        while len(self.player.travel_cards) != 8:
            self.player.travel_cards.append(GAME.traveldeck.draw())
        if len(self.player.transport_cards) < 5:
            card = GAME.transportDeck.draw_faceDown()
            card.isFaceUp = False  # make sure
            self.player.transport_cards.append(card)
        print("reset round command execution")
        self.player.passed = False
        return self.player


class drawTCCommand():
    def __init__(self, player, index):
        self.player = player
        self.index = index

    def execute(self, g):
        from phase3 import Phase3
        p3 = Phase3(self.player)
        self.player, g = p3.execute(self.index, g)
        self.player.command = None
        return self.player, self.index


class placeTCOnPathCommand():
    def __init__(self, player, index):
        self.player = player
        self.index = index

    def execute(self):
        self.player.command = None
        return self.player, self.index


class placeTCOnPathSecondStepCommand():
    def __init__(self, player, index):
        self.player = player
        self.index = index

    def execute(self):
        self.player.command = None
        return self.player, self.index


class moveBootCommand():
    def __init__(self, player):
        self.player = player

    def execute(self, GAME):
        x = self.player.clicked[0]
        y = self.player.clicked[1]
        moved, error = self.player.move(x, y, GAME)
        # print("###command.py, returning if moved (a little funky), most importantly, the error num: ", str(error))
        return self.player, moved, error


class moveBoot_BasicOrCaravan():
    def __init__(self, player):
        self.player = player

    def execute(self):
        print("###command.py, Stepping into executing moveBoot_BasicOrCaravan")
        if self.player.clickedBasic() and not self.player.tried_moving:
            print("###command.py, checking if clickedBasic is true.")
            self.player.command = moveBootCommand(self.player)
            return self.player
        elif self.player.clickedCaravan():
            if len(self.player.travel_cards) < 3:
                self.player.message_box = "Not enough Cards for Caravan."
                self.player.command = None
                return self.player
            print("###command.py, checking if clickedCaravan is true.")
            self.player.choosing_caravan_town = True
            # self.player.command = select_caravan_town(self.player)
            self.player.message_box = "Select a Town to move to."
            print("###command.py, Changed Command to drawing caravan cards.")
            return self.player
        return self.player


class select_caravan_town():
    def __init__(self, player):
        self.player = player

    def execute(self, game):
        x = self.player.clicked[0]
        y = self.player.clicked[1]
        valid, obs = self.player.set_caravan_town(x, y, game)
        if valid:
            if obs:
                self.player.message_box = "Select 4 Travel Cards. [Obstacle on Path]"
            else:
                self.player.message_box = "Select 3 Travel Cards."
            self.player.command = None
            self.player.choosing_caravan_town = False
            self.player.choosing_caravan_cards = True
            return self.player, valid
        elif not valid and obs:
            self.player.message_box = "Not enough Travel Cards to go here."
        else:
            self.player.message_box = "Invalid selection."
            return self.player, valid


class moveBoot_LandOrWater():
    def __init__(self, player):
        self.player = player

    def execute(self):
        print("###command.py, Stepping into executing moveBoot_LandOrWater")
        if self.player.clickedLand():
            print("###command.py, checking if clickedLand is true.")
            moved , self.player= self.player.moveOnRoad(self.player.pathDuringChoice[0])
            # self.player.command = moveBoot_BasicOrCaravan(self.player)
            return self.player, moved
        elif self.player.clickedWater():
            moved ,self.player = self.player.moveOnWater(self.player.pathDuringChoice[1])
            # self.player.command = moveBoot_BasicOrCaravan(self.player)
            return self.player, moved

        print("###command.py,moveboot_land_or_water, bad return moving into moveBootCommand")
        # self.player.command = moveBootCommand(self.player)
        return self.player, False


# class moveBoot_CaravanCommand():
#     def __init__(self, player):
#         self.player = player
#         # self.town_selection = town_selection
#
#     def execute(self):
#         x = self.player.clicked[0]
#         y = self.player.clicked[1]
#         moved, error = self.player.move_caravan()
#         return self.player, moved, error


class drawCaravanCardsCommand():
    def __init__(self, player):
        self.player = player

    def execute(self):
        # self.player.message_box = str("Successfully Caravaned.")
        self.player.choosing_caravan_cards = False
        # self.player.choosing_caravan_town = True
        _, _ = self.player.move_caravan()
        self.player.choosing_caravan_cards = False
        self.player.selected_caravan_cards.clear()
        self.player.command = None
        return self.player


class saveGameCommand():
    def __init__(self, gameName,host,game_id) :
        self.gameName = gameName
        self.host = host
        self.game_id = game_id

    def execute(self,game):
        saveGame(game, self.gameName,self.host,self.game_id)


def saveGame(g,id,creator,game_id):
    import base64
    import requests
    import http.client
    import json
    IP = "10.121.120.252"
    conn = http.client.HTTPConnection(IP + ':4242')
    headers = {'Content-Type': 'application/json', 'authorization': 'Basic YmdwLWNsaWVudC1uYW1lOmJncC1jbGllbnQtcHc='}
    url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + "Elfanland" + '&password=' + "Group_11"
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    # print(x.json())
    service_access_token = validate_url(x.json()['access_token'])
    players_field = []
    for player in g.players:
        players_field.append(player.name)
    print(players_field)

    if g.variant == Variant.elfenland_org or g.variant == Variant.elfenland_4 or g.variant == Variant.elfenland_destination_4 or g.variant == Variant.elfenland_destination:
        gamename_field = "Elfenland"
    else:
        gamename_field ="Elfengold"
    
    body = {"gamename": gamename_field,"players": players_field, "savegameid": id}
    conn.request('PUT', '/api/gameservices/Elfenland/savegames/' + str(id) + '?access_token=' + service_access_token, json.dumps(body), headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    if data != b'Savegame can not be added. Id is already in use.':
        ## do not save duplicate files
        serialised = pickle.dumps(g)
        encoded = base64.b64encode(serialised)
        # print(encoded)
        data = {"id": id, "host": creator, "gameid": game_id ,"game": encoded.decode('utf-8')}
        with open("savedGames.json",'r+',encoding='utf-8') as file:
            file_data = json.load(file)        
            # print(file_data)
            file_data["savedGames"].append(data)
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    else:
        serialised = pickle.dumps(g)
        encoded = base64.b64encode(serialised)
        # print(encoded)
        data = {"id": id, "host": creator, "gameid": game_id ,"game": encoded.decode('utf-8')}
        with open("savedGames.json",'r+',encoding='utf-8') as file:
            file_data = json.load(file)        
            # print(file_data)
            
            for savedGame in file_data["savedGames"]:
                if savedGame["id"] == id:
                    file_data["savedGames"].remove(savedGame)
            file_data["savedGames"].append(data)
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)


def validate_url(org):
    if "+" in org:
        org = org.replace("+", "%2B")
    return org


class removeTCCommand():
    def __init__(self, player, index):
        self.player = player
        self.index = index

    def execute(self):
        if self.index != -1 and len(self.player.transport_cards) > 1 and self.index < len(self.player.transport_cards ):
            self.player.transport_cards.pop(self.index)
            self.player.clicked = [0, 0]
        i = self.index
        self.index = -1
        return self.player, i


class loadGameCommand():
    def __init__(self,game_id) :
        self.game_id = game_id

    def execute(self):
        return loadGame(self.game_id)

def loadGame(id):
    import base64
    import json
    with open("savedGames.json",'r',encoding='utf-8') as file:
        file_data = json.load(file)  
        all_games = file_data["savedGames"]   
        for game in all_games:
            if game["id"] == id:
                data = game["game"]
                b = data.encode("utf-8")
                b = base64.b64decode(b)
                g = pickle.loads(b)
    return g
