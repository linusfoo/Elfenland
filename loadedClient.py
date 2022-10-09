import math
from turtle import update
import pygame
# from factory import Factory
from phase3 import Phase3
from travelCard import TravelCardName
from transportCounter import TransportCounterName
from network import Network
import os
from contextlib import contextmanager
import easygui
from tkinter import Event, Tk, Variable, simpledialog
import time
import socket
from phase1 import Phase1
from factory import Town_Factory, Path_Factory
from phase import execute
from Game import Game
from variant import Variant
from command import *
import copy

global PLAYER1_BOOT
global PLAYER2_BOOT
global POINTS_1
global POINTS_2




def main(username,variant,numPlayers,host,game_id,saveID):
    run = True
    n = Network()
    FPS = 80
    WIDTH, HEIGHT = 1435, 850
    MAP_WIDTH = 900
    MAP_HEIGHT = 650
    LEFT_BORDER_WIDTH = 80
    TOP_BORDER_WIDTH = 80

    pygame.init()
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))

    @contextmanager
    def tk(timeout=500):
        root = Tk()  # default roots
        root.withdraw()  # remove from the screen

        # destroy all widgets in `timeout` seconds
        func_id = root.after(int(1000 * timeout), root.quit)
        try:
            yield root
        finally:  # cleanup
            root.after_cancel(func_id)  # cancel callback
            root.destroy()

    # -----------------------------------------------------------------------------------------------------------------
    screen_width =  1435
    screen_height = 850
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color Select")

    # Initialize constants
    font = pygame.font.SysFont("calibri", 30)
    smallfont = pygame.font.SysFont("calibri", 14)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185)
    blackish = (10, 10, 10)
    white = (255, 255, 255)
    black = (0, 0, 0)
    # -------------------------
    NAVY_BLUE = (42, 93, 142)
    r1 = (205, 79, 57)
    r2 = (255, 99, 71)
    g1 = (84, 139, 84)
    g2 = (154, 255, 154)
    y1 = (238, 232, 170)
    y2 = (255, 255, 0)
    b1 = (24, 116, 205)
    b2 = (30, 144, 255)
    bl1 = (40, 40, 40)
    bl2 = (20, 20, 20)
    p1 = (137, 104, 205)
    p2 = (171, 130, 255)

    # Function to create a button
    def create_button(x, y, width, height, hovercolor, defaultcolor):
        mouse = pygame.mouse.get_pos()
        # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
        click = pygame.mouse.get_pressed(3)
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(screen, hovercolor, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(screen, defaultcolor, (x, y, width, height))

 
    
    GAME = n.getP()[0]
    p = n.getP()[1]
    p.command = loadGameCommand(saveID)
    GAME.isSavedGame = True
    m = n.send([GAME, p])
    GAME = m[0]
    

    # m = n.send([GAME, p])
    # print(p.name)

    
    # time.sleep(2)

    # -----------------------------------------------------------------------------------------------------------------

    def update_resources(players):

        ret = []
        for player in players:
            if player.colour != '':
                BOOT = pygame.image.load(
                    os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                BOOT = pygame.transform.scale(BOOT, (30, 30))
                BOOT = pygame.transform.rotate(BOOT, 90)
                POINTS = pygame.image.load(
                    os.path.join(sourceFileDir + '/assets', 'böppel-' + player.colour + '.png'))
                POINTS = pygame.transform.scale(POINTS, (10, 10))
            else:
                BOOT = pygame.image.load(
                    os.path.join(sourceFileDir + '/assets', 'boot-' + 'red' + '.png'))
                BOOT = pygame.transform.scale(BOOT, (0, 0))
                # PLAYER2_BOOT = pygame.transform.rotate(PLAYER2_BOOT, 90)
                POINTS = pygame.image.load(
                    os.path.join(sourceFileDir + '/assets', 'böppel-' + 'red' + '.png'))
                POINTS = pygame.transform.scale(POINTS, (0, 0))
            ret.append([BOOT, POINTS])
        return ret

    CLOSE_GAME = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'UI_Close Game.png'))
    MENU_BUTTON = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'UI_Menu-Button.png'))
    NOT_VISIBLE = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'UI_Not-Visible.png'))

    # UI-IMPORTS

    OS = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Defaults', 'Opponent_Status.png'))
    OSV = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Defaults', 'Opponent_Status_Vert.png'))
    DASH = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Defaults', 'Dashboard.png'))
    MASK = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Defaults', 'Hidden_Card.png'))
    MSGBOX = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/', 'Front_MessageBox.png'))

    # Round Cards.
    ROUND_ONE = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'R1.png'))
    ROUND_TWO = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'R2.png'))
    ROUND_THREE = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'R3.png'))
    ROUND_FOUR = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'R4.png'))



    # Colours
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    DARK_BLUE = (0, 0, 128)
    NAVY_BLUE = (42, 93, 142)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    BOARD_MAP = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'map-Sticker.png'))
    BOARD_MAP = pygame.transform.scale(BOARD_MAP, (MAP_WIDTH, MAP_HEIGHT))

    ROUND_CARDS = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'round-cards.png'))

    PASS_BUTTON = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'Pass_Button.png'))

    WATER_BUTTON = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'Button_Water.png'))

    LAND_BUTTON = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'Button_Land.png'))

    MOVE_CHOICE_BUTTON = pygame.image.load(
        os.path.join(sourceFileDir + '/assets', 'Button_MoveChoice.png'))

    def displayRoundCards(screen, game):
        place = (869, 124)
        if game.currRound == 1:
            screen.blit(pygame.transform.scale(ROUND_ONE, (70, 103)), place)
        if game.currRound == 2:
            screen.blit(pygame.transform.scale(ROUND_TWO, (70, 103)), place)
        if game.currRound == 3:
            screen.blit(pygame.transform.scale(ROUND_THREE, (70, 103)), place)
        if game.currRound == 4:
            screen.blit(pygame.transform.scale(ROUND_FOUR, (70, 103)), place)





    # 884, 47
    def displayOpPoints(screen, player):
        point_val = 0
        x = 20
        while player.pointNum < x and x >= 0:
            point_val += 1
            x -= 1

        font = pygame.font.Font('freesansbold.ttf', 50)
        points = font.render(str(point_val), True, (169, 109, 30))
        screen.blit(points, (884, 47))

    def displayOp2Points(screen, player):
        point_val = 0
        x = 20
        while player.pointNum < x and x >= 0:
            point_val += 1
            x -= 1

        font = pygame.font.Font('freesansbold.ttf', 50)
        points = font.render(str(point_val), True, (169, 109, 30))
        screen.blit(points, (383, 47))

    def change_boot_colour(player, colour):  # for the other player
        player.colour = colour

    def displaycurrPoints(screen, player):
        point_val = 0
        x = 20
        while player.pointNum < x and x >= 0:
            point_val += 1
            x -= 1

        font = pygame.font.Font('freesansbold.ttf', 45)
        points = font.render(str(point_val), True, (169, 109, 30))
        screen.blit(points, (1355, 36))

    def displayCurrName(players):
        while True:
            for player in players:
                if p.player_num == player.player_num:
                    curr_name = font.render(p.name, True, slategrey)
                    screen.blit(curr_name, (1140, 10))
                    if player.colour != '':
                        DISPLAYBOOT = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                        DISPLAYBOOT= pygame.transform.scale(DISPLAYBOOT, (30,30))
                        DISPLAYBOOT = pygame.transform.rotate(DISPLAYBOOT, 90)
                        screen.blit(DISPLAYBOOT, (1025,34))
                    return

    def displayCurrDest(players):
        while True:
            for player in players:
                if p.player_num == player.player_num:
                    curr_name = font.render( p.destinationTown.name, True, slategrey)
                    screen.blit(curr_name, (1140, 35))
                    return
     

    def displayOppResource(players):
        i = 0
        while i < 36:
            for player in players:
                if player.player_num != p.player_num:
                    dispOppTransportCounter(screen,player)


                point_val = 0
                x = 20
                while player.pointNum < x and x >= 0:
                    point_val += 1
                    x -= 1

                font2 = pygame.font.Font('freesansbold.ttf', 50) # for points

                points = font2.render(str(point_val), True, (169, 109, 30))
                if player.player_num == (p.player_num + 1)%6:
                    curr_name = font.render(player.name, True, slategrey)
                    screen.blit(curr_name, (600, 730))
                    

                    if GAME.variant == Variant.elfenland_destination or GAME.variant == Variant.elfenland_destination_4:
                        dest_town = font.render(player.destinationTown.name, True, slategrey)
                        screen.blit(dest_town, (750, 730))
                        screen.blit(points, (890, 757))
                    if GAME.currPlayerNum == player.player_num:
                        SCREEN.blit(CURR_OPP, (500, 720))
                    if player.colour != '':
                        DISPLAYBOOT = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                        DISPLAYBOOT= pygame.transform.scale(DISPLAYBOOT, (30,30))
                        DISPLAYBOOT = pygame.transform.rotate(DISPLAYBOOT, 90)
                        screen.blit(DISPLAYBOOT, (525,743))

                if player.player_num == (p.player_num + 2)%6:
                    curr_name = font.render(player.name, True, slategrey)
                    screen.blit(curr_name, (100, 730))
                   
                    if GAME.variant == Variant.elfenland_destination or GAME.variant == Variant.elfenland_destination_4:
                        dest_town = font.render(player.destinationTown.name, True, slategrey)
                        screen.blit(dest_town, (250, 730))
                        screen.blit(points, (392, 756))
                    if GAME.currPlayerNum == player.player_num:
                        SCREEN.blit(CURR_OPP, (0, 720))
                    if player.colour != '':
                        DISPLAYBOOT = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                        DISPLAYBOOT= pygame.transform.scale(DISPLAYBOOT, (30,30))
                        DISPLAYBOOT = pygame.transform.rotate(DISPLAYBOOT, 90)
                        screen.blit(DISPLAYBOOT, (29,743))
                    

                if player.player_num == (p.player_num + 3)%6:
                    curr_name = font.render(player.name, True, slategrey)
                    curr_name = pygame.transform.rotate(curr_name, 270)
                    screen.blit(curr_name, (55, 302))
                   
                    if GAME.variant == Variant.elfenland_destination or GAME.variant == Variant.elfenland_destination_4:
                        dest_town = font.render(player.destinationTown.name, True, slategrey)
                        dest_town = pygame.transform.rotate(dest_town, 270)
                        screen.blit(dest_town, (55 ,450))
                        points = pygame.transform.rotate(points, 270)
                        screen.blit(points, (20, 601))
                    if GAME.currPlayerNum == player.player_num:
                        rotated = pygame.transform.rotate(CURR_OPP, 270)
                        SCREEN.blit(rotated, (0, 200))
                    if player.colour != '':
                        DISPLAYBOOT = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                        DISPLAYBOOT= pygame.transform.scale(DISPLAYBOOT, (30,30))
                        DISPLAYBOOT = pygame.transform.rotate(DISPLAYBOOT, 90)
                        screen.blit(DISPLAYBOOT, (24,228))
                        
                if player.player_num== (p.player_num + 4)%6:
                    curr_name = font.render(player.name, True, slategrey)
                    screen.blit(curr_name, (100, 10))
                    
                    
                    if GAME.variant == Variant.elfenland_destination or GAME.variant == Variant.elfenland_destination_4:
                        dest_town = font.render(player.destinationTown.name, True, slategrey)
                        screen.blit(dest_town, (250, 10))
                        screen.blit(points, (383, 47))
                    if GAME.currPlayerNum == player.player_num:
                        SCREEN.blit(CURR_OPP, (0, 12))
                    if player.colour != '':
                        DISPLAYBOOT = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                        DISPLAYBOOT= pygame.transform.scale(DISPLAYBOOT, (30,30))
                        DISPLAYBOOT = pygame.transform.rotate(DISPLAYBOOT, 90)
                        screen.blit(DISPLAYBOOT, (27,34))
                        
                if player.player_num == (p.player_num + 5)%6:
                    curr_name = font.render(player.name, True, slategrey)
                    screen.blit(curr_name, (600, 10))
                    
                    if GAME.variant == Variant.elfenland_destination or GAME.variant == Variant.elfenland_destination_4:
                        dest_town = font.render(player.destinationTown.name, True, slategrey)
                        screen.blit(dest_town, (750, 10))
                    screen.blit(points, (884, 47))
                    if GAME.currPlayerNum == player.player_num:
                        SCREEN.blit(CURR_OPP, (500, 12))
                    if player.colour != '':
                        DISPLAYBOOT = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'boot-' + player.colour + '.png'))
                        DISPLAYBOOT= pygame.transform.scale(DISPLAYBOOT, (30,30))
                        DISPLAYBOOT = pygame.transform.rotate(DISPLAYBOOT, 90)
                        screen.blit(DISPLAYBOOT, (527,37))


            i+=1

    # Opponent's Transport Counter Imports
    O_DTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_Dragon.png'))
    O_ECTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_ElfCycle.png'))
    O_HTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_Hidden.png'))
    O_MCTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_MagicCloud.png'))
    O_TTTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_TreeTrunk.png'))
    O_TWTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_TrollWagon.png'))
    O_UTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_Unicorn.png'))
    O_GPTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_GiantPig.png'))
    O_Place = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Small_TransportCounters', 'S_O_Place_Place.png'))

    def showAvailablePlacements(screen, player):
        for path in Path_Factory().paths:
            if path.transportCounter is None:
                screen.blit(O_Place, (path.tcx, path.tcy))



    def dispOppTransportCounter(screen, player):
        if player.player_num == (p.player_num + 5)%6:
            Slots = [(592, 43), (647, 43), (699, 43), (751, 43), (803, 43)]
        if player.player_num == (p.player_num + 4)%6:
            adj = 647 - 592
            x2 = 92
            Slots = [(x2, 43), (x2 + adj, 43), (x2 + adj * 2, 43), (x2 + adj * 3, 43), (x2 + adj * 4, 43)]
        if player.player_num == (p.player_num + 2)%6:
            adj = 647 - 592
            x2 = 92
            Slots = [(x2, 755), (x2 + adj, 755), (x2 + adj * 2, 755), (x2 + adj * 3, 755), (x2 + adj * 4, 755)]
        if player.player_num == (p.player_num + 1)%6:
            adj = 647 - 592
            x2 = 592
            Slots = [(x2, 755), (x2 + adj, 755), (x2 + adj * 2, 755), (x2 + adj * 3, 755), (x2 + adj * 4, 755)]
        if player.player_num == (p.player_num + 3)%6:
            adj = 647 - 592
            y2 = 288
            Slots = [(6, y2), (6, y2 + adj), (6, y2 + adj*2), (6, y2 + adj*3), (6, y2 + adj*4)]
        i = 0

        # Check through the opponent 1's deck
        for transportCounter in player.transport_cards:
            # print("client line 354: " + str(i))
            if transportCounter.name == TransportCounterName.dragon:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_DTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.giantPig:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_GPTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.magicCloud:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_MCTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.elfcycle:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_ECTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.unicorn:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_UTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.trollWagon:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_TWTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.treeTrunk:
                if not transportCounter.isFaceUp:
                    screen.blit(O_HTC, Slots[i])
                else:
                    screen.blit(O_TTTC, Slots[i])
                i += 1

    # Transport Counter Imports
    DTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'Dragon.png'))
    ECTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'EflCycle.png'))
    HTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'Hidden.png'))
    MCTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'MagicCloud.png'))
    TTTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'TreeTrunk.png'))
    TWTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'TrollWagon.png'))
    UTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'Unicorn.png'))
    GPTC = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/TransportCounters', 'GiantPig.png'))

    def dispTransportCounter(screen, player):
        Slots = [(1017, 460), (1100, 460), (1182, 460), (1264, 460), (1346, 460)]
        i = 0
        # Check through the deck
        for transportCounter in player.transport_cards:
            if transportCounter.name == TransportCounterName.dragon and i < 5:
                screen.blit(DTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.giantPig and i < 5:
                screen.blit(GPTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.magicCloud and i < 5:
                screen.blit(MCTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.elfcycle and i < 5:
                screen.blit(ECTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.unicorn and i < 5:
                screen.blit(UTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.trollWagon and i < 5:
                screen.blit(TWTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.treeTrunk and i < 5:
                screen.blit(TTTC, Slots[i])
                i += 1
        if player.obstacle_counter is not None:
            screen.blit(OBS, (989, 710))

    def displayGameTC(screen, game):
        Slots = [(1035, 121), (1130, 121), (1214, 121), (1035, 187), (1130, 187), (1214, 187)]
        i = 0
        # Check through the deck
        for transportCounter in game.transportDeck.faceup_cards:
            if transportCounter.name == TransportCounterName.dragon and i < 5:
                screen.blit(DTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.giantPig and i < 5:
                screen.blit(GPTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.magicCloud and i < 5:
                screen.blit(MCTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.elfcycle and i < 5:
                screen.blit(ECTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.unicorn and i < 5:
                screen.blit(UTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.trollWagon and i < 5:
                screen.blit(TWTC, Slots[i])
                i += 1
            elif transportCounter.name == TransportCounterName.treeTrunk and i < 5:
                screen.blit(TTTC, Slots[i])
                i += 1

        screen.blit(pygame.transform.scale(O_HTC, (60, 61)), Slots[5])


    def displayTransportCountersOnMap(screen, game): # Also displays the obstacles
        for path in game.AllPaths.paths:
            if path.transportCounter is not None:
                # print("#############################")
                # print("#############################")
                # print(path.town1.name, path.town2.name)
                # print("#############################")
                # print("#############################")
                Slot = (path.tcx, path.tcy)
                if path.transportCounter.name == TransportCounterName.dragon:
                    screen.blit(O_DTC, Slot)
                elif path.transportCounter.name == TransportCounterName.giantPig:
                    screen.blit(O_GPTC, Slot)
                elif path.transportCounter.name == TransportCounterName.magicCloud:
                    screen.blit(O_MCTC, Slot)
                elif path.transportCounter.name == TransportCounterName.elfcycle:
                    screen.blit(O_ECTC, Slot)
                elif path.transportCounter.name == TransportCounterName.unicorn:
                    screen.blit(O_UTC, Slot)
                elif path.transportCounter.name == TransportCounterName.trollWagon:
                    screen.blit(O_TWTC, Slot)
                elif path.transportCounter.name == TransportCounterName.treeTrunk:
                    screen.blit(O_TTTC, Slot)
                if path.has_obstacle:
                    screen.blit(OBS_MAP, (path.tcx + 12, path.tcy + 12))


    def countTravelCards(screen, player):

        # Travel Card Counter
        giantPigCount_val = 0
        magicCloudCount_val = 0
        dragonCount_val = 0
        trollWagonCount_val = 0
        elfCycleCount_val = 0
        raftCount_val = 0
        unicornCount_val = 0

        # Check through the deck
        for travelCard in player.travel_cards:
            if travelCard.name == TravelCardName.dragon:
                dragonCount_val += 1
            elif travelCard.name == TravelCardName.giantPig:
                giantPigCount_val += 1
            elif travelCard.name == TravelCardName.magicCloud:
                magicCloudCount_val += 1
            elif travelCard.name == TravelCardName.elfcycle:
                elfCycleCount_val += 1
            elif travelCard.name == TravelCardName.unicorn:
                unicornCount_val += 1
            elif travelCard.name == TravelCardName.trollWagon:
                trollWagonCount_val += 1
            elif travelCard.name == TravelCardName.raft:
                raftCount_val += 1

        font = pygame.font.Font('freesansbold.ttf', 15)

        # First Row
        # Giant Pig Counter
        giantPigCount = font.render(str(giantPigCount_val), True, white)
        screen.blit(giantPigCount, (1084, 535))

        if giantPigCount_val == 0:
            screen.blit(MASK, (1016, 540))  # Don't TouchF

        # Magic Cloud Counter
        magicCloudCount = font.render(str(magicCloudCount_val), True, white)
        screen.blit(magicCloudCount, (1188, 535))

        if magicCloudCount_val == 0:
            screen.blit(MASK, (1119, 540))  # Don't Touch

        # Dragon Counter
        dragonCount = font.render(str(dragonCount_val), True, white)
        screen.blit(dragonCount, (1291, 534))

        if dragonCount_val == 0:
            screen.blit(MASK, (1222, 540))  # Don't Touch

        # Troll Wagon Counter
        trollWagonCount = font.render(str(trollWagonCount_val), True, white)
        screen.blit(trollWagonCount, (1397, 535))

        if trollWagonCount_val == 0:
            screen.blit(MASK, (1329, 540))  # Don't Touch

        # Second Row

        # Elf Cycle Counter
        elfCycleCount = font.render(str(elfCycleCount_val), True, white)
        screen.blit(elfCycleCount, (1132, 682))

        if elfCycleCount_val == 0:
            screen.blit(MASK, (1063, 687))  # Don't Touch

        # Raft Counter
        raftCount = font.render(str(raftCount_val), True, white)
        screen.blit(raftCount, (1234, 681))

        if raftCount_val == 0:
            screen.blit(MASK, (1168, 686))  # Don't Touch

        # Unicorn Counter
        unicornCount = font.render(str(unicornCount_val), True, white)
        screen.blit(unicornCount, (1339, 682))

        if unicornCount_val == 0:
            screen.blit(MASK, (1271, 687))  # Don't Touch

    def displayPlayerMessage(screen, player):
        if player.message_box is not None:
            font = pygame.font.Font('freesansbold.ttf', 15)
            message = font.render(str(player.message_box), True, (169, 109, 30))
            screen.blit(message, (100, 820))

    # def saveGameName():


    CLNT = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/turns', 'A_Client.png'))
    CURR_CLNT = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/turns', 'A_Curr_Client.png'))
    OPP = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/turns', 'A_Opp.png'))
    CURR_OPP = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/turns', 'A_Curr_Opp.png'))
    VERT_OPP = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/turns', 'A_Vert_Opp.png'))
    CURR_VERT_OPP = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/turns', 'A_Curr_vert_Opp.png'))

    def displayCurrPlayer(currPlayer,game):
        i = game.currPlayerNum
        if i == currPlayer.player_num:
            SCREEN.blit(CURR_CLNT, (1000, 12))
        # elif i == 1:
        #     SCREEN.blit(CURR_OPP, (0, 12))
        # elif i == 2:
        #     SCREEN.blit(CURR_OPP, (500, 12))
        # The rest need to be implemented.

    OBS_HOLDER = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Obstacle', 'o_Holder.png'))
    OBS = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Obstacle', 'o_Obs.png'))
    OPP_OBS_HOLDER = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Obstacle', 'o_Opp_Holder.png'))
    OPP_OBS = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Obstacle', 'o_Opp_Obs.png'))
    OBS_MAP = pygame.image.load(
        os.path.join(sourceFileDir + '/assets/Obstacle', 'o_Obs_map.png'))

    def redrawWindow(screen, players, game):
        pygame.display.set_caption("Player " + str(p.player_num))
        player = players[0]
        # player2 = players[1]
        # player3 = players[2]
        resources = update_resources(players)
        screen.fill(NAVY_BLUE)
        screen.blit(BOARD_MAP, (LEFT_BORDER_WIDTH, TOP_BORDER_WIDTH))
        # screen.blit(ROUND_CARDS, (850, 100))


        i = 0
        for i in range(0, len(resources)):
            screen.blit(resources[i][0], (players[i].town.width + i * 3, players[i].town.height + i * 3))
            for points in players[i].points:
                screen.blit(resources[i][1], (points.town.width + i * 3, points.town.height + i * 3))


        # Global coordinate adjustments for obsactle
        adj_x = 93
        adj_y = 7
        # OPPONENT STATUS ON TOP
        SCREEN.blit(OS, (0, 12))
        SCREEN.blit(OPP, (0, 12))
        SCREEN.blit(OPP_OBS_HOLDER, (0 + adj_x, 12 + adj_y))  # Use these to place obstacle transport counter on UI

        SCREEN.blit(OS, (500, 12))
        SCREEN.blit(OPP, (500, 12))
        SCREEN.blit(OPP_OBS_HOLDER, (500 + adj_x, 12 + adj_y))


        # OPPONENT STATUS ON THE LEFT
        SCREEN.blit(OSV, (0, 200))
        SCREEN.blit(VERT_OPP, (0, 200))
        SCREEN.blit(OPP_OBS_HOLDER, (0 + adj_y, 200 + adj_x)) # Use this specially again.


        # OPPONENT STATUS ON BOTTOM
        SCREEN.blit(OS, (0, 720))
        SCREEN.blit(OPP, (0, 720))
        SCREEN.blit(OPP_OBS_HOLDER, (0 + adj_x, 720 + adj_y))

        SCREEN.blit(OS, (500, 720))
        SCREEN.blit(OPP, (500, 720))
        SCREEN.blit(OPP_OBS_HOLDER, (500 + adj_x, 720 + adj_y))


        # USER STATUS
        SCREEN.blit(DASH, (1000, 12))
        SCREEN.blit(CLNT, (1000, 12))
        screen.blit(PASS_BUTTON, (944, 323))
        screen.blit(WATER_BUTTON, (1367, 402))
        screen.blit(LAND_BUTTON, (1367, 296))
        screen.blit(MOVE_CHOICE_BUTTON, (1354, 692))
        screen.blit(MSGBOX, (0, 807))
        screen.blit(OBS_HOLDER, (980, 700)) #994 711


        ##########################
        ##ADD UPDATE CYCLES HERE##
        ##########################
        if GAME.variant == Variant.elfenland_destination:
            displayCurrDest(players)
            # displayOppDest(players)

        displayCurrPlayer(player, game)
        displayCurrName(players)
        displayOppResource(players)
        displayGameTC(SCREEN, game)
        showAvailablePlacements(SCREEN, player)
        countTravelCards(SCREEN, player)
        dispTransportCounter(SCREEN, player)

        displaycurrPoints(SCREEN, player)
        displayTransportCountersOnMap(SCREEN, game)
        displayPlayerMessage(SCREEN, player)
        displayRoundCards(SCREEN, game)
        pygame.display.update()

    # pygame.mixer.music.load(sourceFileDir + '/assets/background_sound.mp3')
    CLICK_SOUND = pygame.mixer.Sound(sourceFileDir + '/assets/click_sound.mp3')
    ERROR_SOUND = pygame.mixer.Sound(sourceFileDir + '/assets/error_sound.mp3')
    CLAP_SOUND = pygame.mixer.Sound(sourceFileDir + '/assets/applause.mp3')

    clock = pygame.time.Clock()

    def main_game(p, opponents, GAME):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and p.name == host:
                if event.key == pygame.K_s:
                    print("SAVING GAME")
                    # from tkinter import 
                    # with tk(timeout=2000):
                    #     easygui.msgbox('\n\n\n\n               Winner: ' )
                    # 
                    # the input dialog
                    root = Tk()
                    # center root window
                    root.eval('tk::PlaceWindow . center')
                    root.withdraw()

                    USER_INP = simpledialog.askstring(title="ID",
                                                    prompt="What would you like the Game ID to be?", parent=root)

                    # # check it out
                    p.command = saveGameCommand(USER_INP, host,game_id)

                    #TODO need to remove screen after and stop
                    GAME.update(p)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                print("Player phase num: ", GAME.currentPhase)

                pygame.mixer.Sound.play(CLICK_SOUND)
                print(GAME.currPlayerNum)
            
                if GAME.currPlayerNum == p.player_num or GAME.currentPhase == 6:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    p.clicked = [x, y]
                    print(x,y)
                    # GAME.lastEdit = p.player_num
                    p, opponents, GAME = execute(GAME.currentPhase, p, opponents, GAME)
                    # 
        return p, opponents, GAME

    # GAME = n.getP()[0]
    p.command = reSetUpCommand(username)
    p = p.command.execute(GAME)
    p.command = reSetUpCommand(username)
    GAME.update(p)
    m = n.send([GAME, p])
    GAME = m[0]
    # p = p.command.execute(GAME)
    print(p.name)
    CLICK = [0,0]
    currNum = p.player_num
    ROOT = Tk()
    ROOT.withdraw()
    while run:
        pygame.event.poll()
        
        clock.tick(60)
        GAME.update(p)
        m = n.send([GAME, p])
        if (m!= None):
            GAME.copyData(m[0])
            p = GAME.players[currNum]
            p.clicked = CLICK
            if not GAME.end and GAME.winner == None:
                ps = copy.deepcopy(GAME.players)
                for a in ps:
                    if a.player_num == p.player_num:
                        ps.remove(a)
                opponents = ps
                redrawWindow(SCREEN, [p] + opponents, GAME)
                if p.ready :  #and p2.ready      
                    p, opponents, GAME = main_game(p, opponents, GAME)
                    CLICK = p.clicked
            else:
                with tk(timeout=2000):
                    easygui.msgbox('\n\n\n\n               Winner: ' + 'linus2')
                    sleep(2)
                    pygame.quit()


if __name__ == '__main__':
    import sys

    main(sys.argv)
