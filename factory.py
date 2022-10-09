# from eifanland import ELVENHOLD
# from locatable import Locatable
from road_type import Road_Type
from town import Town
from path import Path
from point import Point


#create towns, roads and create adjacent town
# class Factory():

class Town_Factory():

    def __init__(self):
        self.towns = []
        self.TICHIH = Town(770 ,182,"Tichih",3)
        self.THROTMANNI = Town(612, 250,"Throtmanni",3)
        self.RIVINIA = Town(726 ,325,"Rivinia",3)
        self.ELVENHOLD = Town(766, 448,"Elvenhold",0)
        self.FEODOR = Town(563 ,388,"Feodor",4)
        self.LAPPHALYA = Town(570,530, "Lapphalya",2)
        self.ERGEREN = Town(900, 335,"Ergeren",5)
        self.BEATA = Town(906 ,553,"Beata",2)
        self.STRYKHAVEN = Town(802, 607,"Strykhaven",4)
        self.VIRST = Town(634 ,645,"Virst",3)
        self.JACCARANDA = Town(459, 177,"Jaccaranda",5)
        self.ALBARAN = Town(416, 361,"Albaran",7)
        self.DAGAMURA = Town(420,483, "Dagamura",4)
        self.JXARA = Town(406, 639, "Jxara",3)
        self.MAHDAVIKIA= Town(201, 620, "Mahdavikia",5)
        self.GRANGOR= Town(165 ,495, "Grangor",5)
        self.KIHROMAH= Town(294, 449, "Kihromah",6)
        self.YTTAR= Town(141 ,354, "Yttar",4)
        self.PARUNDIA= Town(303 ,294, "Parundia",4)
        self.USSELEN= Town(151, 215, "Usselen",4)
        self.WYLHIEN= Town(304, 140, "Wyhlien",3)


        self.towns.append(self.TICHIH)


        self.towns.append(self.RIVINIA)

        self.towns.append(self.ELVENHOLD)

        self.towns.append(self.FEODOR)

        self.towns.append(self.LAPPHALYA)

        self.towns.append(self.ERGEREN)

        self.towns.append(self.BEATA)

        self.towns.append(self.STRYKHAVEN)

        self.towns.append(self.VIRST)

        self.towns.append(self.JACCARANDA)

        self.towns.append(self.ALBARAN)

        self.towns.append(self.DAGAMURA)

        self.towns.append(self.JXARA)

        self.towns.append(self.MAHDAVIKIA)

        self.towns.append(self.GRANGOR)

        self.towns.append(self.KIHROMAH)

        self.towns.append(self.YTTAR)

        self.towns.append(self.PARUNDIA)

        self.towns.append(self.USSELEN)

        self.towns.append(self.WYLHIEN)

        self.towns.append(self.THROTMANNI)

        self.RIVINIA.add_adj(self.TICHIH)
        self.RIVINIA.add_adj(self.THROTMANNI)
        self.RIVINIA.add_adj(self.FEODOR)
        self.RIVINIA.add_adj(self.LAPPHALYA)
        self.RIVINIA.add_adj(self.ELVENHOLD)
        self.RIVINIA.add_adj(self.THROTMANNI)

        self.TICHIH.add_adj(self.THROTMANNI)
        self.TICHIH.add_adj(self.ERGEREN)
        self.TICHIH.add_adj(self.RIVINIA)
        self.TICHIH.add_adj(self.JACCARANDA)

        self.ERGEREN.add_adj(self.TICHIH)
        self.ERGEREN.add_adj(self.ELVENHOLD)

        self.BEATA.add_adj(self.ELVENHOLD)
        self.BEATA.add_adj(self.STRYKHAVEN)

        self.ELVENHOLD.add_adj(self.ERGEREN)
        self.ELVENHOLD.add_adj(self.TICHIH)
        self.ELVENHOLD.add_adj(self.RIVINIA)
        self.ELVENHOLD.add_adj(self.LAPPHALYA)
        self.ELVENHOLD.add_adj(self.BEATA)
        self.ELVENHOLD.add_adj(self.STRYKHAVEN)
        self.ELVENHOLD.add_adj(self.VIRST)

        self.STRYKHAVEN.add_adj(self.VIRST)
        self.STRYKHAVEN.add_adj(self.BEATA)
        self.STRYKHAVEN.add_adj(self.ELVENHOLD)

        self.VIRST.add_adj(self.STRYKHAVEN)
        self.VIRST.add_adj(self.ELVENHOLD)
        self.VIRST.add_adj(self.LAPPHALYA)
        self.VIRST.add_adj(self.JXARA)

        self.LAPPHALYA.add_adj(self.ELVENHOLD)
        self.LAPPHALYA.add_adj(self.VIRST)
        self.LAPPHALYA.add_adj(self.JXARA)
        self.LAPPHALYA.add_adj(self.DAGAMURA)
        self.LAPPHALYA.add_adj(self.FEODOR)
        self.LAPPHALYA.add_adj(self.RIVINIA)

        self.FEODOR.add_adj(self.LAPPHALYA)
        self.FEODOR.add_adj(self.ELVENHOLD)
        self.FEODOR.add_adj(self.DAGAMURA)
        self.FEODOR.add_adj(self.RIVINIA)
        self.FEODOR.add_adj(self.ALBARAN)
        self.FEODOR.add_adj(self.THROTMANNI)

        self.THROTMANNI.add_adj(self.ALBARAN)
        self.THROTMANNI.add_adj(self.RIVINIA)
        self.THROTMANNI.add_adj(self.TICHIH)
        self.THROTMANNI.add_adj(self.JACCARANDA)
        self.THROTMANNI.add_adj(self.FEODOR)

        self.JACCARANDA.add_adj(self.THROTMANNI)
        self.JACCARANDA.add_adj(self.TICHIH)
        self.JACCARANDA.add_adj(self.WYLHIEN)

        self.ALBARAN.add_adj(self.PARUNDIA)
        self.ALBARAN.add_adj(self.WYLHIEN)
        self.ALBARAN.add_adj(self.THROTMANNI)
        self.ALBARAN.add_adj(self.FEODOR)
        self.ALBARAN.add_adj(self.DAGAMURA)

        self.DAGAMURA.add_adj(self.ALBARAN)
        self.DAGAMURA.add_adj(self.KIHROMAH)
        self.DAGAMURA.add_adj(self.FEODOR)
        self.DAGAMURA.add_adj(self.LAPPHALYA)
        self.DAGAMURA.add_adj(self.MAHDAVIKIA)
        self.DAGAMURA.add_adj(self.JXARA)

        self.JXARA.add_adj(self.MAHDAVIKIA)
        self.JXARA.add_adj(self.DAGAMURA)
        self.JXARA.add_adj(self.LAPPHALYA)
        self.JXARA.add_adj(self.VIRST)

        self.MAHDAVIKIA.add_adj(self.JXARA)
        self.MAHDAVIKIA.add_adj(self.DAGAMURA)
        self.MAHDAVIKIA.add_adj(self.GRANGOR)
        self.MAHDAVIKIA.add_adj(self.VIRST)

        self.GRANGOR.add_adj(self.YTTAR)
        self.GRANGOR.add_adj(self.PARUNDIA)
        self.GRANGOR.add_adj(self.MAHDAVIKIA)

        self.KIHROMAH.add_adj(self.DAGAMURA)

        self.YTTAR.add_adj(self.GRANGOR)
        self.YTTAR.add_adj(self.PARUNDIA)
        self.YTTAR.add_adj(self.USSELEN)

        self.USSELEN.add_adj(self.YTTAR)
        self.USSELEN.add_adj(self.PARUNDIA)
        self.USSELEN.add_adj(self.WYLHIEN)
        self.USSELEN.add_adj(self.YTTAR)

        self.PARUNDIA.add_adj(self.YTTAR)
        self.PARUNDIA.add_adj(self.GRANGOR)
        self.PARUNDIA.add_adj(self.ALBARAN)
        self.PARUNDIA.add_adj(self.WYLHIEN)
        self.PARUNDIA.add_adj(self.USSELEN)

        self.WYLHIEN.add_adj(self.USSELEN)
        self.WYLHIEN.add_adj(self.PARUNDIA)
        self.WYLHIEN.add_adj(self.ALBARAN)
        self.WYLHIEN.add_adj(self.JACCARANDA)



    def getTown(self, pname):
        fac = Town_Factory()
        for town in fac.towns:
            if town.name == pname:
                return town

    def getTowns(self):
        return self.towns

class Point_Factory():


    def __init__(self):
        import pygame
        import os
        from client import sourceFileDir
        self.one = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-01.png'))
        self.two= pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-02.png'))
        self.three = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-03.png'))
        self.four = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-04.png'))
        self.five = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-05.png'))
        self.six = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-06.png'))
        self.seven = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-07.png'))
        self.eight = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-08.png'))
        self.nine = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-09.png'))
        self.ten = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-10.png'))
        self.eleven = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-11.png'))
        self.twelve = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-12.png'))
        self.thirteen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-13.png'))
        self.fourteen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-14.png'))
        self.fifteen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-15.png'))
        self.sixteen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-16.png'))
        self.seventeen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-17.png'))
        self.eighteen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-18.png'))
        self.nineteen = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-19.png'))
        self.twenty = pygame.image.load(os.path.join(sourceFileDir + '/assets', 'Score-20.png'))

    def get_point(self, number):
            if number == 1:
                return self.one
            if number == 2:
                return self.two
            if number == 3:
                return self.three
            if number == 4:
                return self.four
            if number == 5:
                return self.five
            if number == 6:
                return self.six
            if number == 7:
                return self.seven
            if number == 8:
                return self.seven
            if number == 9:
                return self.eight
            if number == 10:
                return self.ten
            if number == 11:
                return self.eleven
            if number == 12:
                return self.twelve
            if number == 13:
                return self.thirteen
            if number == 14:
                return self.fourteen
            if number == 15:
                return self.fifteen
            if number == 16:
                return self.sixteen
            if number == 17:
                return self.seventeen
            if number == 18:
                return self.eighteen
            if number == 19:
                return self.nineteen
            if number == 20:
                return self.twenty


class WaterWay_Factory():
    def __init__(self):
        from path import WaterWay
        from road_type import WaterWay_Type
        towns = Town_Factory()

        self.water_ways = []


        self.Virst_Jxara = WaterWay(towns.VIRST, towns.JXARA, WaterWay_Type.DOWNSTREAM)
        self.water_ways.append(self.Virst_Jxara)

        self.Jxara_Virst = WaterWay(towns.JXARA, towns.VIRST, WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Jxara_Virst)

        self.Jxara_Mahdavika = WaterWay(towns.JXARA, towns.MAHDAVIKIA, WaterWay_Type.DOWNSTREAM)
        self.water_ways.append(self.Jxara_Mahdavika)

        self.Mahdavika_Jxara = WaterWay(towns.MAHDAVIKIA, towns.JXARA,  WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Mahdavika_Jxara)

        self.Mahdavika_Grangor = WaterWay(towns.MAHDAVIKIA, towns.GRANGOR,  WaterWay_Type.DOWNSTREAM)
        self.water_ways.append(self.Mahdavika_Grangor)

        self.Grangor_Mahdavika = WaterWay(towns.GRANGOR, towns.MAHDAVIKIA,  WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Grangor_Mahdavika)

        self.Grangor_Yttar = WaterWay(towns.YTTAR, towns.GRANGOR, WaterWay_Type.LAKE)
        self.water_ways.append(self.Grangor_Yttar)

        self.Yttar_Grangor = WaterWay(towns.GRANGOR, towns.YTTAR, WaterWay_Type.LAKE)
        self.water_ways.append(self.Grangor_Yttar)

        self.Yttar_Parundia = WaterWay(towns.YTTAR, towns.PARUNDIA, WaterWay_Type.LAKE)
        self.water_ways.append(self.Yttar_Parundia)

        self.Parundia_Yttar = WaterWay(towns.PARUNDIA, towns.YTTAR, WaterWay_Type.LAKE)
        self.water_ways.append(self.Parundia_Yttar)

        self.Grangor_Parundia =  WaterWay(towns.GRANGOR, towns.PARUNDIA, WaterWay_Type.LAKE)
        self.water_ways.append(self.Grangor_Parundia)

        self.Parundia_Grangor = WaterWay(towns.PARUNDIA, towns.GRANGOR, WaterWay_Type.LAKE)
        self.water_ways.append(self.Parundia_Grangor)

        self.Usselen_Wylhien = WaterWay(towns.USSELEN, towns.WYLHIEN, WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Usselen_Wylhien)

        self.Wylhien_Usselen = WaterWay(towns.WYLHIEN, towns.USSELEN, WaterWay_Type.DOWNSTREAM)
        self.water_ways.append(self.Wylhien_Usselen)

        self.Virst_Strykhaven = WaterWay(towns.VIRST, towns.STRYKHAVEN, WaterWay_Type.LAKE)
        self.Strykhaven_Virst = WaterWay(towns.STRYKHAVEN, towns.VIRST, WaterWay_Type.LAKE)
        self.water_ways.append(self.Virst_Strykhaven)
        self.water_ways.append(self.Strykhaven_Virst)

        self.Elvenhold_Virst = WaterWay(towns.ELVENHOLD, towns.VIRST, WaterWay_Type.LAKE)
        self.Virst_Elvenhold = WaterWay(towns.VIRST, towns.ELVENHOLD, WaterWay_Type.LAKE)
        self.water_ways.append(self.Elvenhold_Virst)
        self.water_ways.append(self.Virst_Elvenhold)

        self.Strykhaven_Elvenhold = WaterWay(towns.STRYKHAVEN, towns.ELVENHOLD, WaterWay_Type.LAKE)
        self.Elvenhold_Strykhaven = WaterWay(towns.ELVENHOLD, towns.STRYKHAVEN, WaterWay_Type.LAKE)
        self.water_ways.append(self.Strykhaven_Elvenhold)
        self.water_ways.append(self.Elvenhold_Strykhaven)

        self.Beata_Elvenhold = WaterWay(towns.BEATA, towns.ELVENHOLD, WaterWay_Type.DOWNSTREAM)
        self.Elvenhold_Beata = WaterWay(towns.ELVENHOLD, towns.BEATA, WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Beata_Elvenhold)
        self.water_ways.append(self.Elvenhold_Beata)

        self.Elvenhold_Rivinia = WaterWay(towns.ELVENHOLD, towns.RIVINIA, WaterWay_Type.DOWNSTREAM)
        self.Rivinia_Elvenhold = WaterWay(towns.RIVINIA, towns.ELVENHOLD, WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Elvenhold_Rivinia)
        self.water_ways.append(self.Rivinia_Elvenhold)

        self.Rivinia_Tichih = WaterWay(towns.RIVINIA, towns.TICHIH, WaterWay_Type.DOWNSTREAM)
        self.Tichih_Rivinia = WaterWay(towns.TICHIH, towns.RIVINIA, WaterWay_Type.UPSTREAM)
        self.water_ways.append(self.Tichih_Rivinia)
        self.water_ways.append(self.Rivinia_Tichih)

    # def getWaterWay(self, currTown, desTown):
    #     for way in self.water_ways:
    #         if way.town1 is currTown and way.town2 is desTown:
    #             return way


    def getAllWays(self):
        return self.water_ways




class Path_Factory():
    def __init__(self):
        from path import Path
        from road_type import Road_Type
        towns = Town_Factory()

        self.paths = []
    	
        # Elvenhold -> #3
        self.Elvenhold_Lapphalaya = Path(towns.ELVENHOLD, towns.LAPPHALYA, Road_Type.PLAIN, 650, 480)
        self.paths.append(self.Elvenhold_Lapphalaya) #(666, 497)

        self.Elvenhold_Beata = Path(towns.ELVENHOLD, towns.BEATA, Road_Type.PLAIN, 835, 495)
        self.paths.append(self.Elvenhold_Beata) #(841, 501)

        self.Elvenhold_Ergeren = Path(towns.ELVENHOLD, towns.ERGEREN, Road_Type.WOOD, 868, 370)
        self.paths.append(self.Elvenhold_Ergeren) #(882, 388)

        # Lapphalaya -> #5
        self.Lapphalaya_Virst = Path(towns.LAPPHALYA, towns.VIRST, Road_Type.PLAIN, 558, 573)
        self.paths.append(self.Lapphalaya_Virst) #(579, 58)

        self.Lapphalaya_Jxara = Path(towns.LAPPHALYA, towns.JXARA, Road_Type.WOOD, 463, 568)
        self.paths.append(self.Lapphalaya_Jxara) #(479, 590)

        self.Lapphalaya_Dagamaru = Path(towns.LAPPHALYA, towns.DAGAMURA, Road_Type.WOOD, 475, 502)
        self.paths.append(self.Lapphalaya_Dagamaru) #(477, 520)

        self.Lapphalaya_Rivinia = Path(towns.LAPPHALYA, towns.RIVINIA, Road_Type.WOOD, 644, 385)
        self.paths.append(self.Lapphalaya_Rivinia) #(477, 520)

        self.Lapphalaya_Feodor = Path(towns.LAPPHALYA, towns.FEODOR, Road_Type.WOOD, 563, 420)
        self.paths.append(self.Lapphalaya_Feodor) #(576, 449)

        # Beata -> #1
        self.Beata_Strykhaven = Path(towns.BEATA, towns.STRYKHAVEN, Road_Type.PLAIN, 883, 590) # 883,602
        self.paths.append(self.Beata_Strykhaven) #(883, 609)

        # Strykhaven -> #1
        self.Strykhaven_Virst = Path(towns.VIRST, towns.STRYKHAVEN, Road_Type.MOUNTAIN, 715, 650)
        self.paths.append(self.Strykhaven_Virst) #(715, 680)

        # Virst -> #1
        self.Virst_Jxara = Path(towns.VIRST, towns.JXARA, Road_Type.PLAIN, 481, 655)
        self.paths.append(self.Virst_Jxara)  #(481, 655)

        # JXARA -> #2
        self.Jxara_Dagamaru = Path(towns.DAGAMURA, towns.JXARA, Road_Type.WOOD, 374, 547)
        self.paths.append(self.Jxara_Dagamaru)  #(389, 559)

        self.Jxara_Mahdavika = Path(towns.MAHDAVIKIA, towns.JXARA, Road_Type.MOUNTAIN, 259, 621)
        self.paths.append(self.Jxara_Mahdavika)  #(272, 638)

        # MAHDAVIKA -> #2
        self.Mahdavika_Dagamaru = Path(towns.MAHDAVIKIA, towns.DAGAMURA, Road_Type.MOUNTAIN, 268, 533)
        self.paths.append(self.Mahdavika_Dagamaru)  #(289, 552)

        self.Mahdavika_Grangor = Path(towns.MAHDAVIKIA, towns.GRANGOR, Road_Type.MOUNTAIN, 122, 550)
        self.paths.append(self.Mahdavika_Grangor)  #(137, 563)

        # GRANGOR -> #1
        self.Grangor_Yttar = Path(towns.YTTAR, towns.GRANGOR, Road_Type.MOUNTAIN, 115, 397)
        self.paths.append(self.Grangor_Yttar)  #(139, 426)

        # YTTAR -> #1
        self.Yttar_Usselen = Path(towns.YTTAR, towns.USSELEN, Road_Type.WOOD, 126, 243)
        self.paths.append(self.Yttar_Usselen)  #(153, 270)

        # USSELEN -> #2
        self.Usselen_Parundia = Path(towns.PARUNDIA, towns.USSELEN, Road_Type.WOOD, 197, 222)
        self.paths.append(self.Usselen_Parundia)  #(210, 258)

        self.Usselen_Wylhien = Path(towns.WYLHIEN, towns.USSELEN, Road_Type.PLAIN, 178, 125)
        self.paths.append(self.Usselen_Wylhien) #(189, 140)

        # PARUNDIA -> #2
        self.Parundia_Albaran = Path(towns.PARUNDIA, towns.ALBARAN, Road_Type.DESERT, 355, 287)
        self.paths.append(self.Parundia_Albaran) #(362, 317)

        self.Parundia_Wylhien = Path(towns.PARUNDIA, towns.WYLHIEN, Road_Type.PLAIN, 260, 206)
        self.paths.append(self.Parundia_Wylhien) #(275, 215)

        # ALBARAN -> #4
        self.Albaran_Dagamaru = Path(towns.DAGAMURA, towns.ALBARAN, Road_Type.DESERT, 393, 397)
        self.paths.append(self.Albaran_Dagamaru) #(411, 414)

        self.Albaran_Feodor = Path(towns.FEODOR, towns.ALBARAN, Road_Type.DESERT, 475, 343)
        self.paths.append(self.Albaran_Feodor) #(490, 359)

        self.Albaran_Wylhien = Path(towns.WYLHIEN, towns.ALBARAN, Road_Type.DESERT, 338, 205)
        self.paths.append(self.Albaran_Wylhien) #(376, 237)

        self.Albaran_Throtmani = Path(towns.THROTMANNI, towns.ALBARAN, Road_Type.DESERT, 485, 282)
        self.paths.append(self.Albaran_Throtmani) #(501, 301)

        # THROTMANNI #4
        self.Throtmani_Jaccaranda = Path(towns.THROTMANNI, towns.JACCARANDA, Road_Type.MOUNTAIN, 499, 194)
        self.paths.append(self.Throtmani_Jaccaranda) #(495, 214)

        self.Throtmani_Tichih = Path(towns.THROTMANNI, towns.TICHIH, Road_Type.PLAIN, 667, 199)
        self.paths.append(self.Throtmani_Tichih) #(700, 230)

        self.Throtmani_Rivinia = Path(towns.THROTMANNI, towns.RIVINIA, Road_Type.WOOD, 656, 258)
        self.paths.append(self.Throtmani_Rivinia) #(669, 274)

        self.Throtmani_Feodor = Path(towns.THROTMANNI, towns.FEODOR, Road_Type.DESERT, 544, 296)
        self.paths.append(self.Throtmani_Feodor) #(544, 296)

        # WYLHIEN #1
        self.Wylhien_Jaccaranda = Path(towns.WYLHIEN, towns.JACCARANDA, Road_Type.MOUNTAIN, 349, 109)
        self.paths.append(self.Wylhien_Jaccaranda) #[389, 143]

        # JACCARANDA #1
        self.Jaccaranda_Tichih = Path(towns.TICHIH, towns.JACCARANDA, Road_Type.MOUNTAIN, 560, 144)
        self.paths.append(self.Jaccaranda_Tichih) #[612, 169]

        # TICHIH #1
        self.Tichih_Ergeren = Path(towns.TICHIH, towns.ERGEREN, Road_Type.WOOD, 826, 252)
        self.paths.append(self.Tichih_Ergeren) #[839, 275]

        # RIVINIA #1
        self.Rivinia_Feodor = Path(towns.RIVINIA, towns.FEODOR, Road_Type.WOOD, 603, 324)
        self.paths.append(self.Rivinia_Feodor) #[622, 360]

        # DAGAMARU #1
        self.Dagamaru_Kihroma = Path(towns.DAGAMURA, towns.KIHROMAH, Road_Type.WOOD, 331, 431)
        self.paths.append(self.Dagamaru_Kihroma)
        self.Dagamaru_Feodor = Path(towns.DAGAMURA, towns.FEODOR, Road_Type.DESERT, 452, 403)
        self.paths.append(self.Dagamaru_Feodor)




    def getPaths(self):
        return self.paths

    # def getPath(self, currTown, desTown):
    #     for path in self.paths:
    #         if (path.town1 is currTown and path.town2 is desTown) or (path.town1 is currTown and path.town2 is desTown):
    #             return path
    #         else:
    #             print("Didn't find any")
    #             continue



class Travel_Card_Factory():


    def __init__(self):
        from travelCard import TravelCard, TravelCardName
        self.dragon = TravelCard(TravelCardName.dragon)
        self.unicorn = TravelCard(TravelCardName.unicorn)
        self.troll_wagon = TravelCard(TravelCardName.trollWagon)
        self.elfcycle = TravelCard(TravelCardName.elfcycle)
        self.magic_cloud = TravelCard(TravelCardName.magicCloud)
        self.giant_pig = TravelCard(TravelCardName.giantPig)
        self.raft = TravelCard(TravelCardName.raft)
        self.witch = TravelCard(TravelCardName.witch)

class Transport_Card_Factory():

    def __init__(self):
        from transportCounter import TransportCounter, TransportCounterName
        self.dragon = TransportCounter(TransportCounterName.dragon)
        self.unicorn = TransportCounter(TransportCounterName.unicorn)
        self.troll_wagon = TransportCounter(TransportCounterName.trollWagon)
        self.elfcycle = TransportCounter(TransportCounterName.elfcycle)
        self.magic_cloud = TransportCounter(TransportCounterName.magicCloud)
        self.giant_pig = TransportCounter(TransportCounterName.giantPig)
        self.obstacle = TransportCounter(TransportCounterName.obstacle)
        self.goldpiece = TransportCounter(TransportCounterName.goldpiece)
        self.seaMonsterObstacle = TransportCounter(TransportCounterName.seaMonsterObstacle)
        self.double = TransportCounter(TransportCounterName.double)
        self.exchange = TransportCounter(TransportCounterName.exchange)





