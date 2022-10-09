import copy
from shutil import move
import socket
from _thread import *
import sys

from numpy import var
from egphase2 import Phase2
from phase3 import Phase3
from phase4 import Phase4
from phase5 import Phase5s
from player import Player
from factory import Town_Factory
import pickle
from transportCounterDeck import TransportCounterDeck
from travelCardDeck import TravelCardDeck
from variant import Variant
from egphase1 import Phase1
from Game import Game
from command import *

# server = "10.0.0.202"
# server = "10.121.181.187"
server = "localhost"
port = 6000
TOWN_FACTORY = Town_Factory()
ELVENHOLD = TOWN_FACTORY.ELVENHOLD
g = Game([Player(0, '', ELVENHOLD), Player(1, '', ELVENHOLD), Player(2, '', ELVENHOLD),Player(3, '', ELVENHOLD), 
Player(4, '', ELVENHOLD), Player(5, '', ELVENHOLD)], Variant.elfengold_org)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        a = pickle.dumps([g, g.players[idx]])
        conn.send(a)
        reply = ""
        while True:
            
            try:
                phase3Completed = False
                data = pickle.loads(conn.recv(2048 * 256))
                
                if data[0].currentPhase == 0:
                    print(data[0].currRound)
                    phase1 = Phase1(data[0])
                    phase2 = Phase2(data[0])
                    phase1.execute()
                    data[0] = phase2.execute()
                    data[0].currentPhase = 3
                for player in data[0].players:
                    if player.command != None:
                        if isinstance(player.command, drawTCCommand):
                            print("• Initializing Phase3")
                            player, index = player.command.execute()
                            p3 = Phase3(player)
                            player, g = p3.execute(index, g)
                            # if all([player.phase_num == 4 for player in data[0].players]):
                            #     print("• Phase3 is complete.")
                            g.players[player.player_num] = player
                            if len(player.transport_cards) == 5 and g.currPlayerNum == player.player_num:
                                if player.player_num == len(g.players) - 1:
                                    g.currPlayerNum = 0
                                    g.currentPhase = 4
                                else:
                                    g.currPlayerNum += 1
                                    print(g.currPlayerNum)
                        elif isinstance(player.command, changeColourCommand):
                            g.players[player.player_num], variant,numPlayers = player.command.execute()
                            g.avail_colours.remove(player.colour)
                            if numPlayers != None:
                                g = g.removePlayer(numPlayers)

                            if variant != None:
                                g = g.changeVariant(variant)
                            
                            
                        elif isinstance(player.command, placeTCOnPathCommand) and data[0].currentPhase == 4 and g.currPlayerNum == player.player_num:
                            player, index = player.command.execute()
                            print("• Initializing Phase4")
                            phase4 = Phase4(player)
                            id = -1
                            if player.clickedPass():
                                print("passed")
                                player.command = None
                                g.passed.append(player)
                                print(len(g.passed))
                                if len(g.passed) >= len(g.players):
                                    g.currentPhase = 5
                                    g.currPlayerNum = 0
                                    g.passed = []
                                elif player.player_num == len(g.players) -1:
                                    g.currPlayerNum = 0
                                    # g.passed.append(player)
                                else:
                                    g.currPlayerNum += 1
                                    # g.passed.append(player)
                                g.update(player)

                            elif id == -1:
                                x = player.clicked[0]
                                y = player.clicked[1]
                                print("player clicked this shit: ", player.clicked)

                                if x > 983 and y > 457 and y < 521:
                                    print("• Player chose a transport counter. ")
                                    id = phase4.clickedTransportCard(x, y)
                                    print("Idx: ", id)
                                    print("Chosen transport card: ", player.transport_cards[id].name)
                                    player.chosenTCidxForPhase4 = id
                                    player.command = placeTCOnPathSecondStepCommand(player, index)
                                    g.players[player.player_num] = player
                                    print(" • Player's command is onto the second step.")
                                else:
                                    print("• Invalid Selection. ")
                                    id = -1

                        elif isinstance(player.command,
                                        placeTCOnPathSecondStepCommand) and g.currPlayerNum == player.player_num and not player.passed:
                           
                            phase4 = Phase4(player)
                            # print("player num" + str(player.player_num))
                            # print("Prompt: Please select a tile.")
                            x = player.clicked[0]
                            y = player.clicked[1]
                            # print("player clicked this shit: ", player.clicked)
                            if player.clickedPass():
                                print("passed")
                                player.command = None
                                g.passed.append(player)
                                if len(g.passed) >= len(g.players):
                                    g.currentPhase = 5
                                    g.currPlayerNum = 0
                                    g.passed = []
                                elif player.player_num == len(g.players)-1:
                                    g.currPlayerNum = 0
                                    # g.passed.append(player)
                                else:
                                    g.currPlayerNum += 1
                                    # g.passed.append(player)
                                g.update(player)

                        
                            if x < 983:
                                set = False
                                player, g, set = phase4.setTransportCounters(player.chosenTCidxForPhase4, x, y, g)
                                if set:
                                    player.command = None
                                    print("• System has set the Transport Counter to a chosen path.")
                                    g.passed = []
                                    if player.player_num == len(g.players)-1:
                                        g.currPlayerNum = 0
                                    else:
                                        g.currPlayerNum += 1
                                        print(g.currPlayerNum)
                                    player.command = None
                                    g.update(player)
                                    # if g.currPlayerNum == 2:
                                    #     g.currentPhase = 5
                        elif isinstance(player.command, moveBootCommand) and g.currPlayerNum == player.player_num:
                            print("• Initializing Phase5")
                            if player.clickedPass():
                                player.passed = True
                                g.passed.append(player)
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                                        g.endGame()
                                        ##DECLARE WINNER
                                    else:
                                        g.currRound += 1
                                        g.currentPhase = 0
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                elif player.player_num == len(g.players)-1:
                                    g.currPlayerNum = 0
                                    
                                else:
                                    g.currPlayerNum += 1
                                    # g.passed.append(player)
                                player.command = None
                                g.update(player)
                            else:
                                player, moved, er = player.command.execute(g)
                                if moved and er == 0: # If the error number is 0, then it moved. Alternatively, error of 2 prompts choice of land or water.
                                    g.update(player)
                                elif moved and er == 2:
                                    print("#204##server.py, Error number is 2 and player's command is being changed to moveBoot_LandOrWater")
                                    player.command = moveBoot_LandOrWater(player)
                                    g.update(player)
                                g.players[player.player_num] = player
                        elif isinstance(player.command, moveBoot_LandOrWater) and g.currPlayerNum == player.player_num:
                            if player.clickedPass():
                                player.passed = True
                                if len(g.passed) == len(g.players):
                                    if g.currRound == g.numOfRounds:
                                        g.endGame()
                                        ##DECLARE WINNER
                                    else:
                                        g.currRound += 1
                                        g.currentPhase = 0
                                        g.currPlayerNum = 0
                                        g.cleanMap()  # Removes all the Transport Counters on the map.
                                        g.passed = []
                                elif player.player_num == len(g.players)-1:
                                    g.currPlayerNum = 0
                                    g.passed.append(player)
                                else:
                                    g.currPlayerNum += 1
                                    g.passed.append(player)
                                player.command = None
                                g.update(player)
                            else:
                                print("Stepping into executing moveBoot_LandOrWater")
                                player, moved = player.command.execute()
                                if moved:
                                    g.update(player)
                                g.players[player.player_num] = player

                        elif isinstance(player.command, moveBootThreeTCs) and g.currPlayerNum == player.player_num:
                            if player.clickedPass():
                                player.command = moveBootCommand(player)
                            else:
                                phase5 = Phase5(player)
                                selected = []
                                for i in range(0, 3):
                                    selected.append(phase5.selectTravelCards())
                                phase5.updateAssets(player)
                            player, moved = player.command.execute(g)   # !moved == passed

                if not data:
                    print("Disconnected")
                    break
                else:
                    reply = copy.deepcopy(g.players)
                    for p in reply:
                        if p.player_num == idx:
                            reply.remove(p)
        
                conn.sendall(pickle.dumps([g, reply]))
            except Exception as e:
                pass

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