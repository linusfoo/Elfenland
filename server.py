import copy
from shutil import move
import socket
from _thread import *
import sys

from phase2 import Phase2
from phase3 import Phase3
from phase4 import Phase4
from phase5 import Phase5
from player import Player
from factory import Town_Factory
import pickle
from transportCounterDeck import TransportCounterDeck
from travelCardDeck import TravelCardDeck
from variant import Variant
from phase1 import Phase1
from Game import Game
from command import *


# server = "10.0.0.202"

server = "10.121.120.252"
port = 6000
TOWN_FACTORY = Town_Factory()
ELVENHOLD = TOWN_FACTORY.ELVENHOLD
g = Game([Player(0, '', ELVENHOLD), Player(1, '', ELVENHOLD), Player(2, '', ELVENHOLD), Player(3, '', ELVENHOLD),
          Player(4, '', ELVENHOLD), Player(5, '', ELVENHOLD)], Variant.elfenland_org)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def validate_url(org):
    if "+" in org:
        org = org.replace("+", "%2B")
    return org



def main():
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)
    # global TransportDeck

    s.listen()
    print("Waiting for a connection, Server Started")

    phase1 = Phase1(g)
    phase2 = Phase2(g)
    if phase1.finished is False:
        phase1.execute()
    if phase2.finished is False and phase1.finished is True:
        phase2.execute()

    def threaded_client(conn, idx):
        
        global g
        # g = getGame()
        global newIDX
        newIDX = -1
        a = pickle.dumps([g, g.players[idx]])
        conn.send(a)
        reply = ""
        while True:
            
            if newIDX !=-1:
                idx = newIDX
            try:
                phase3Completed = False
                data = pickle.loads(conn.recv(2048 * 256))
                
                if data[0].isSavedGame:
                    for player in data[0].players:
                        if isinstance(player.command, loadGameCommand):
                            data[0] = player.command.execute()
                            player.command = None
                            # data[0].isSavedGame = False
                            g = data[0]
                            


                if data[0].currentPhase == 6: # thread issue
                    for p in g.players:
                        for player in data[0].players:
                            if p.player_num == player.player_num:
                                if len(player.transport_cards) > len(p.transport_cards):
                                    player.transport_cards = p.transport_cards

                if data[0].currentPhase == 5:
                    for p in g.players:
                        for player in data[0].players:
                            # if not isinstance(player.command,select_caravan_town) and not isinstance(p.command,select_caravan_town):
                            if p.player_num == player.player_num:
                                if p.town.name != player.town.name:
                                    player= p
                                    data[0].update(player)


                for player in data[0].players:
                    if player.command != None:
                        if isinstance(player.command, drawTCCommand):
                            print("• Initializing Phase3")
                            player, index = player.command.execute(g)
                            g.players[player.player_num] = player
                            if len(player.transport_cards) == 5 and g.currPlayerNum == player.player_num:
                                if player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                    g.currentPhase = 4
                                    for p in g.players:
                                        p.message_box = str("Click on a Transport Counter to place on the board")
                                else:
                                    g.currPlayerNum += 1
                                    # print(g.currPlayerNum)
                            elif index != -1:
                                if player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                else:
                                    g.currPlayerNum += 1
                        elif isinstance(player.command, changeColourCommand):
                            g.players[player.player_num], variant, numPlayers = player.command.execute()
                            g.avail_colours.remove(player.colour)
                            if numPlayers != None:
                                g = g.removePlayer(numPlayers)
                            if variant != None:
                                g = g.changeVariant(variant)
                        elif isinstance(player.command, saveGameCommand):
                            player.command.execute(g)

                        elif isinstance(player.command, reSetUpCommand):
                            newIDX= (player.command.execute(g)).player_num

                        elif isinstance(player.command, placeTCOnPathCommand) and data[0].currentPhase == 4 and g.currPlayerNum == player.player_num:
                            player, index = player.command.execute()
                            print("• Initializing Phase4")
                            phase4 = Phase4(player)
                            id = -1
                            if player.clickedPass():
                                player.message_box = "Pass or choose to move boot the Basic way or Caravan."
                                print("passed")
                                player.command = None
                                g.passed.append(player)
                                # print(len(g.passed))
                                if len(g.passed) >= len(g.players):
                                    g.currentPhase = 5
                                    g.currPlayerNum = 0
                                    g.passed = []
                                elif player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                    # g.passed.append(player)
                                else:
                                    g.currPlayerNum += 1
                                    # g.passed.append(player)
                                g.update(player)
                            elif id == -1:
                                x = player.clicked[0]
                                y = player.clicked[1]
                                # print("Player clicked : ", player.clicked)
                                if (x > 983 and 457 < y < 521) or (1052 > x > 983 and 772 > y >= 710):
                                    print("• Player chose a transport counter. ")
                                    id = phase4.clickedTransportCard(x, y)
                                    print("Idx: ", id)
                                    if 0 <= id and id <= 4:
                                        player.message_box = str("Chosen transport card: " + \
                                                                 str(player.transport_cards[id].name.name).upper() + ". Place it on the board")
                                        player.chosenTCidxForPhase4 = id
                                        player.command = placeTCOnPathSecondStepCommand(player, index)
                                    elif id == 5:
                                        player.message_box = str(
                                            "Chosen transport card: " + str(player.obstacle_counter.name.name).upper())
                                        player.chosenTCidxForPhase4 = id
                                        player.command = placeTCOnPathSecondStepCommand(player, index)
                                    elif id == -5:
                                        player.message_box = "Obstacle already used."
                                    g.players[player.player_num] = player
                                else:
                                    player.message_box = "Invalid Selection."

                        elif isinstance(player.command,
                                        placeTCOnPathSecondStepCommand) and g.currPlayerNum == player.player_num and not player.passed:
                            print("• Initializing Phase4.5")
                            
                            phase4 = Phase4(player)
                            x = player.clicked[0]
                            y = player.clicked[1]
                            if player.clickedPass():
                                print("passed")
                                player.message_box = "Pass or choose to move boot the Basic way or Caravan."
                                player.command = None
                                g.passed.append(player)
                                if len(g.passed) >= len(g.players):
                
                                    p1.message_box = "Click on a town to move to"
                                    g.update(p1)
                                    g.currentPhase = 5
                                    g.currPlayerNum = 0
                                    g.passed = []
                                    
        
                                elif player.player_num == len(g.players)-1:
                                    g.currPlayerNum = 0
                                else:
                                    g.currPlayerNum += 1
                                g.update(player)
                            if x < 983:
                                set = False
                                player, g, set = phase4.setTransportCounters(player.chosenTCidxForPhase4, x, y, g)
                                if set:
                                    player.command = None
                                    print("• System has set the Transport Counter to a chosen path.")
                                    g.passed = []
                                    if player.player_num == len(g.players) - 1:
                                        g.currPlayerNum = 0
                                        player.message_box = str("Click on a Transport Counter to place on the board")
                                    else:
                                        g.currPlayerNum += 1
                                        print(g.currPlayerNum)
                                    player.command = None
                                    g.update(player)

                        # Move Boot
                        elif isinstance(player.command,
                                        moveBoot_BasicOrCaravan) and g.currPlayerNum == player.player_num:
                            print("• Initializing Phase5.1")
                            player.message_box = "Pass or choose to move boot the Basic way or Caravan."
                            if player.clickedPass():
                                player.passed = True
                                g.passed.append(player)
                                player.command = None
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                                        g = g.endGame()
                                        g.end = True
                                        ##DECLARE WINNER
                                    else:
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                        g.currentPhase = 6
                                        g.update(player)
                                elif player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                else:
                                    g.currPlayerNum += 1
                                g.update(player)
                            else:
                                player = player.command.execute()
                                if not isinstance(player.command , moveBootCommand):
                                    player.command = None
                                else:
                                    player.message_box = "Choose a town to move to"
                                g.update(player)
                        elif isinstance(player.command, select_caravan_town) and g.currPlayerNum == player.player_num:
                            print("• Initializing select_caravan_town")
                            if player.clickedPass():
                                player.passed = True
                                g.passed.append(player)
                                player.command = None
                                print(g.currRound , g.numOfRounds)
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                        
                                        p.message_box = "Choose transport cards to remove"
                                        g.update(p)
                                        g = g.endGame()
                                        g.end = True
                                        ##DECLARE WINNER
                                    else:
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                        g.currentPhase = 6
                                        g.update(player)
                                elif player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                else:
                                    g.currPlayerNum += 1
                                g.update(player)
                            else:
                                player, valid = player.command.execute(g)
                                player.command = None
                                g.update(player)
                        elif isinstance(player.command, drawCaravanCardsCommand) and g.currPlayerNum == player.player_num:
                            print("• Initializing Phase5.3")
                            # player.message_box = "Choose 3 Travel Cards to Caravan your way into the next town."
                            p5 = Phase5(player, g)
                            if player.clickedPass():
                                player.passed = True
                                g.passed.append(player)
                                player.command = None
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                                        g = g.endGame()
                                        g.end = True
                                        ##DECLARE WINNER
                                    else:
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                        g.currentPhase = 6
                                        g.update(player)
                                elif player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                else:
                                    g.currPlayerNum += 1
                                g.update(player)
                            else:
                                print("Into the else-block")
                                x = player.clicked[0]
                                y = player.clicked[1]
                                print("server.py, Player's Last Click: ", x, ", ", y)
                                # path = player.getPath(player.town, player.caravan_town, g)
                                # if path.has_obstacle:
                                #     if len(player.selected_caravan_cards) == 4:
                                #         print("Executing caravan movement")
                                #         player = player.command.execute()
                                #     else:
                                if x > 983:
                                    print("checked selected_caravan_cards length: ", len(player.selected_caravan_cards))
                                    t_card, err = p5.selectTravelCards(x, y)
                                    # player.refreshClick()
                                    g.update(player)
                                    # print("After selection, server.py, Player's Last Click: ", x, ", ", y)
                                    print("t_card returned.")
                                    if err == -1:
                                        player.message_box = "Selected card not available."
                                        print("Selected card not available.")
                                    elif err == -2:
                                        player.message_box = "Selected out of bounds."
                                        print("Selected out of bounds.")
                                        player.clickec = [0,0]
                                    else:
                                        # player.refreshClick()
                                        player.message_box = str("Selected TravelCard: " + t_card.name.name).upper()
                                        player = p5.update_selection(t_card)   # This also executes
                                        g.update(player)

    

                                g.update(player)


                    

                        elif isinstance(player.command, moveBootCommand) and g.currPlayerNum == player.player_num:
                            print("• Initializing Phase5.2")
                            # player.message_box = "Pass or choose to move boot the Basic way or Caravan."
                            if player.clickedPass():
                                player.passed = True
                                g.passed.append(player)
                                player.command = None
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                                        g = g.endGame()
                                        g.end = True
                                        ##DECLARE WINNER
                                    else:
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                        g.currentPhase = 6
                                        g.update(player)
                                elif player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                else:
                                    g.currPlayerNum += 1
                                g.update(player)
                            else:
                                player, moved, er = player.command.execute(g)
                                if moved and er == 0:  # If the error number is 0, then it moved. Alternatively, error of 2 prompts choice of land or water.
                                    player.command = None
                                    player.tried_moving = False
                                    player.clicked = [0,0]
                                    g.update(player)

                                elif moved and er == 2:
                                    print(
                                        "#204##server.py, Error number is 2 and player's command is being changed to moveBoot_LandOrWater")
                                    player.command = moveBoot_LandOrWater(player)
                                elif er == -1:  # If the player has a bad choice
                                    player.command = None
                                g.update(player)

                        elif isinstance(player.command, moveBoot_LandOrWater) and g.currPlayerNum == player.player_num:
                            if player.clickedPass():
                                player.passed = True
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                                        g.endGame()
                                        g.end = True
                                        ##DECLARE WINNER
                                    else:
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                        g.currentPhase = 6
                                        g.update(player)
                                elif player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                    g.passed.append(player)
                                else:
                                    g.currPlayerNum += 1
                                    g.passed.append(player)
                                player.command = None
                                player.tried_moving = False
                                g.update(player)
                            else:
                                print("Stepping into executing moveBoot_LandOrWater")
                                player, moved = player.command.execute()
                                if moved:
                                    g.update(player)
                                    player.command = moveBoot_BasicOrCaravan(player)
                                    player.clicked = [0,0]
                                    player.tried_moving = False
                                    player.message_box = "Pass or choose to move boot the Basic way or Caravan."
                                g.players[player.player_num] = player
                        elif isinstance(player.command, removeTCCommand) and g.currentPhase == 6:
                            player, index = player.command.execute()
                            g.update(player)
                            if index != -1:
                                # g.lastEdit = player.player_num
                                if len(player.transport_cards) == 1 and not (player.player_num in g.passed):
                                    g.passed.append(player.player_num)
                                    print("add player")
                            if len(g.passed) == len(g.players):
                                print("restting round")
                                g.resetRound = True
                                g.passed = []
                                break

                if not data:
                    print("Disconnected")
                    break
                else:
                    # print(idx)
                    if g.resetRound:
                        for player1 in g.players:
                            player1 = resetRoundCommand(player1).execute(g)
                            g = g.update(player1)
                            player1.command = None
                            player1.ried_moving = False
                            g.currPlayerNum = 0
                            g.currentPhase = 3
                        g.currRound += 1
                        g.resetRound = False
                    reply = copy.deepcopy(g.players)
                    for p in reply:
                        if p.player_num == idx:
                            reply.remove(p)

                conn.sendall(pickle.dumps([g, reply]))
            except Exception as e:
                print(e)

        print(str(addr) + " Lost connection")
        conn.close()

    currentPlayer = 0
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn, currentPlayer))
        print(currentPlayer)
        currentPlayer += 1


if __name__ == '__main__':
    main()
