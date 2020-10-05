#Морской Бой v1.5.0
import os
import random
import time
from termcolor import colored
import colorama
colorama.init() 
import copy
if os.name == 'nt':
    os.system('mode con:cols=134 lines=38')
Map01 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,2,0,2,0,0,0,0,0,2,2,0,2,2,0,2,2,0,0,1], [1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,0,2,2,0,0,0,0,2,2,0,2,2,0,2,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map02 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,2,0,0,2,0,2,0,0,2,2,0,0,2,2,2,2,0,0,2,1], [1,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,1], [1,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,2,1], [1,0,0,2,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,1], [1,2,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,1], [1,2,0,2,2,2,0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,2,0,2,1], [1,2,0,2,0,0,0,0,0,0,0,2,0,2,2,2,2,0,2,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map03 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,2,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,2,1], [1,2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,0,0,2,0,2,0,0,2,0,0,0,2,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,1], [1,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,2,0,2,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map04 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,2,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,1], [1,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,1],[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,2,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,2,2,2,2,2,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map05 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,2,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,2,2,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,2,2,0,0,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,2,0,2,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map06 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,1], [1,0,2,2,2,2,2,2,0,2,0,2,0,2,2,2,2,2,0,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,2,2,2,2,0,0,0,2,0,2,2,2,2,0,0,1], [1,0,2,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,1], [1,0,0,0,2,0,2,2,2,0,0,2,0,2,0,2,0,2,2,0,0,1], [1,0,0,0,2,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,2,0,0,1], [1,0,0,0,2,0,0,2,0,2,2,2,2,0,0,2,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,1], [1,0,0,2,0,0,0,2,0,0,2,2,0,0,0,2,0,0,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Enemy = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#0 - пустая клетка; 1 - промах, 2 - корабль, 3 - подбитый корабль
PDx = 0
PDy = 0
Side = 0
i = 0
PlayerCount = 77
EnemyCount = 77
Sides=[0,0,0,0,0]
Tactic = 1
KilledAfterDamage = 0

while 1:
    Language = int(input("Выберите Язык (RU - 1; ENG - 2): "))
    if Language == 1:
        Letters = "ЁАБВГДЕЖЗИКЛМНОПРСТУФЙ"
        break
    elif Language == 2:
        Letters = "ЁABCDEFGHIJKLMNOPQRSTЙ"
        break

def RandomMap():
    MapRand = copy.deepcopy(Enemy)
    Ships = [6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for icount in range(0, len(Ships)):
        Angle = random.randint(1,2)
        while 1:
            SomeBolean = 1
            RandX = random.randint(0,21)
            RandY = random.randint(0,21)
            if MapRand[RandX][RandY]==0 and RandX+Ships[icount]<=22 and RandY+Ships[icount]<=22:
                if Angle == 1: 
                    for onemorecount in range (0, Ships[icount]):
                        if MapRand[RandX+onemorecount][RandY] != 0:
                            SomeBolean = 0
                elif Angle == 2: 
                    for onemorecount in range (0, Ships[icount]):
                        if MapRand[RandX][RandY+onemorecount] != 0:
                            SomeBolean = 0
                if SomeBolean == 1: 
                    break
        for onemorecount in range(0,Ships[icount]):
            MapRand[RandX][RandY] = 2
            MapRand[RandX-1][RandY-1] = 1
            MapRand[RandX-1][RandY+1] = 1
            MapRand[RandX+1][RandY-1] = 1
            MapRand[RandX+1][RandY+1] = 1
            if Ships[icount] == 1:
                MapRand[RandX-1][RandY] = 1
                MapRand[RandX][RandY+1] = 1
                MapRand[RandX+1][RandY] = 1
                MapRand[RandX][RandY-1] = 1
            if Angle == 1:
                if onemorecount==0: MapRand[RandX-1][RandY] = 1 
                RandX +=1
                if onemorecount==Ships[icount]-1: MapRand[RandX][RandY] = 1
            elif Angle == 2: 
                if onemorecount==0: MapRand[RandX][RandY-1] = 1 
                RandY +=1
                if onemorecount==Ships[icount]-1: MapRand[RandX][RandY] = 1
    for icount in range (1,21): 
        for jcount in range (1,21):
            if MapRand[icount][jcount]==1:
                MapRand[icount][jcount]=0
    return(MapRand)
        
def Suicide():
    for i in range (1,21): 
        for j in range (1,21):
            if Player[i][j]==2:
                Player[i][j]=3
    PrintField()
    PlayerCount=0
    print("paying respect...")
    if os.name == "nt":
        os.system("pause")
    exit()
    
def Kaboom():
    for i in range (10,12): 
        for j in range (10,12):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (9,13): 
        for j in range (9,13):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (8,14): 
        for j in range (8,14):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (7,15): 
        for j in range (7,15):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (6,16): 
        for j in range (6,16):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (5,17): 
        for j in range (5,17):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (4,18): 
        for j in range (4,18):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (3,19): 
        for j in range (3,19):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (2,20): 
        for j in range (2,20):
            Enemy[i][j]=3
    PrintField()
    time.sleep(0.5)
    for i in range (1,21): 
        for j in range (1,21):
            Enemy[i][j]=3
    EnemyCount=0
    PrintField()
    print("what a mess we made...")
    if os.name == "nt":
        os.system("pause")
    exit()
    
def PrintField (): 
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print(colored("                                      _____              ______         _    _    _                                                  ",'red','on_blue',attrs=['bold']))
    print(colored("              ,:',:`,:',:'          ",'white','on_blue',attrs=['bold'])+colored(" /  ___|             | ___ \       | |  | |  | |                                                 ",'red','on_blue',attrs=['bold']))
    print(colored("           __||_||_||_||__          ",'red','on_blue')+colored(" \ `--.   ___   __ _ | |_/ /  __ _ | |_ | |_ | |  ___                                            ",'red','on_blue',attrs=['bold']))
    print(colored("      ____[\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"]____     ",'red','on_blue',attrs=['bold'])+colored("  `--. \ / _ \ / _` || ___ \ / _` || __|| __|| | / _ \\                                           ",'red','on_blue',attrs=['bold']))
    print(colored("      \ \" '''''''''''''''''''' |    ",'red','on_blue',attrs=['bold'])+colored(" /\__/ /|  __/| (_| || |_/ /| (_| || |_ | |_ | ||  __/ ",'red','on_blue',attrs=['bold'])+colored("  v1.5.0                                  ",'green','on_blue',attrs=['bold']))
    print(colored("    ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^  ",'blue','on_blue',attrs=['bold'])+colored(" \____/  \___| \__,_|\____/  \__,_| \__| \__||_| \___| ",'red','on_blue',attrs=['bold'])+colored("  it just works!                          ",'green','on_blue',attrs=['bold']))
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    if Language == 1:
        print("  |                            Игрок                             ||    |                           Противник                         ")
        print("--|-----------------------------","{:02d}".format(77-PlayerCount),"---------------------------  ||  --|-----------------------------","{:02d}".format(77-EnemyCount),"----------------------------")
        print("--|------------------------------------------------------------  ||  --|-------------------------------------------------------------")
        print("  |  А  Б  В  Г  Д  Е  Ж  З  И  К  Л  М  Н  О  П  Р  С  Т  У  Ф  ||    |  А  Б  В  Г  Д  Е  Ж  З  И  К  Л  М  Н  О  П  Р  С  Т  У  Ф ")
    if Language == 2:
        print("  |                            Player                            ||    |                             Enemy                          ")
        print("--|-----------------------------","{:02d}".format(77-PlayerCount),"---------------------------  ||  --|-----------------------------","{:02d}".format(77-EnemyCount),"----------------------------")
        print("--|------------------------------------------------------------  ||  --|-------------------------------------------------------------")
        print("  |  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  ||    |  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T ")
    print("--|------------------------------------------------------------  ||  --|-------------------------------------------------------------")
    for i in range (1,21): 
        print("{:02d}".format(i),end="")
        print("| ",end="")
        for j in range (1,21): 
            if Player[i][j] == 0:
                print(colored(" ~ ",'blue','on_cyan'),end = "")
            if Player[i][j] == 1:
                print(colored(" # ",'white','on_cyan',attrs=['bold']),end = "")
            if Player[i][j] == 2:
                print(colored(" О ",'green','on_green',attrs=['bold']),end = "")
            if Player[i][j] == 3:
                print(colored(" Х ",'red','on_red',attrs=['bold']),end = "")
        print (" ||  ", end = "" )
        print("{:02d}".format(i),end="")
        print("| ",end="")
        for j in range (1,21): 
            if Enemy[i][j] == 0:
                print(colored(" ~ ",'blue','on_cyan'),end = "")
            if Enemy[i][j] == 1:
                print(colored(" # ",'white','on_cyan',attrs=['bold']),end = "")
            if Enemy[i][j] == 2:
                print(colored(" О ",'green','on_green',attrs=['bold']),end = "")
            if Enemy[i][j] == 3:
                print(colored(" Х ",'red','on_red',attrs=['bold']),end = "") 
        print ()
        
def EnemyTurn ():
    global PlayerCount, EnemyCount
    if PlayerCount <= 0:
        print("YOU STINK LOSER")
        if os.name == "nt":
            os.system("pause")
        exit()
    print("Ход противника.")

    while 1:
        Et = input("Введите координаты: ")
        try:
            for i in range(len(Letters)): 
                if (Et[0].upper()==Letters[i]): Ex = i
            if len(Et) == 2:
                Ey = int(Et[1])
            else:
                Ey = int(Et[1])*10+int(Et[2])
            if Player[Ey][Ex]==2:
                SaveX = Ex
                SaveY = Ey
                SaveS = Player[Ey][Ex]
                Player[Ey][Ex]=3
                PrintField()
                if Player[Ey+1][Ex]==2 or Player[Ey-1][Ex]==2 or Player[Ey][Ex+1]==2 or Player[Ey][Ex-1]==2:
                    print("РАНИЛ")
                else:
                    if Player[Ey+1][Ex]==3:
                        i=2
                        while Player[Ey+i][Ex]==3:
                            i+=1
                        if Player[Ey+i][Ex]==2:
                            print("РАНИЛ")
                        else:
                            print("УБИЛ")
                    elif Player[Ey-1][Ex]==3:
                        i=2
                        while Player[Ey-i][Ex]==3:
                            i+=1
                        if Player[Ey-i][Ex]==2:
                            print("РАНИЛ")
                        else:
                            print("УБИЛ")
                    elif Player[Ey][Ex+1]==3:
                        i=2
                        while Player[Ey][Ex+i]==3:
                            i+=1
                        if Player[Ey][Ex+i]==2:
                            print("РАНИЛ")
                        else:
                            print("УБИЛ")
                    elif Player[Ey][Ex-1]==3:
                        i=2
                        while Player[Ey][Ex-i]==3:
                            i+=1
                        if Player[Ey][Ex-i]==2:
                            print("РАНИЛ")
                        else:
                            print("УБИЛ")
                    else:
                        print("УБИЛ")
                PlayerCount-=1
                if PlayerCount > 0: EnemyTurn()
            else:
                Player[int(Ey)][int(Ex)]=1
                PrintField()
                print("МИМО")
            break
        except:
            PrintField()
            print("Неверная координата")
            
def DeveloperMode (): 
    global Language, PlayerCount, EnemyCount
    while True:
        Command = input("Enter cheat code: ").upper()
        Ex = 0
        Ey = 0
        if Command == "EXIT":
            PrintField()
            break
        elif Command == "LANGRU":
            Language = 1
            Letters = "ЁАБВГДЕЖЗИКЛМНОПРСТУФЙ"
        elif Command == "LANGENG":
            Language = 2
            Letters = "ЁABCDEFGHIJKLMNOPQRSTЙ"
        elif Command == "SUICIDE":
            Suicide()
        elif Command == "KABOOM":
            Kaboom()
        elif Command == "PLAYERCOUNT":
            try: 
                PlayerCount = int(input("Enter PlayerCount: "))
            except: 
                print("Wrong number")
        elif Command == "ENEMYCOUNT":
            try: 
                EnemyCount = int(input("Enter EnemyCount: "))
            except: 
                print("Wrong number")
        else:
            try:
                for i in range(len(Letters)): 
                    if (Command[1]==Letters[i]): Ex = i
                Ey = int(Command[2]+Command[3])
                if Command[0]=='P' or Command[0]=='И':
                    Player[Ey][Ex]=int(Command[4])
                    if int(Command[4]) == 2:
                        PlayerCount+=1
                    if int(Command[4]) == 3:
                        PlayerCount-=1
                elif Command[0]=='E' or Command[0]=='П':
                    Enemy[Ey][Ex]=int(Command[4])
                    if int(Command[4]) == 3:
                        EnemyCount-=1
                else:
                    print("Wrong command")
            except:
                print("Wrong command")
        PrintField()

def PlayerTurnDamaged (Px,Py):
    global PDx, PDy, Side, i, PlayerCount, EnemyCount, Sides, KilledAfterDamage
    while 1:
        if EnemyCount <= 0:
            print("ПОБЕДА")
            if os.name == "nt":
                os.system("pause")
            exit()
        if PDx==0: PDx=Px
        if PDy==0: PDy=Py
        if Side==0: 
            while True:
                Side=random.randint(1,4)
                if Sides[Side]==0:
                    if Side == 1 and Enemy[Py][Px+1]==0:
                        break
                    elif Side == 2 and Enemy[Py+1][Px]==0:
                        break
                    elif Side == 3 and Enemy[Py][Px-1]==0:
                        break
                    elif Side == 4 and Enemy[Py-1][Px]==0:
                        break
        i+=1
        OpositeSide = abs(4-Side)
        if OpositeSide == 2: OpositeSide = 4
        elif OpositeSide == 0: OpositeSide = 2
        if (Enemy[Py][Px]!=0 and Py==21 and Px==21): 
            Sides[Side]=0
            Side = 0
            return
        else:
            if Side == 1: Px+=1 
            elif Side == 2: Py+=1  
            elif Side == 3: Px-=1  
            elif Side == 4: Py-=1
            if Language == 1:
                print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
                print("М - мимо, Р - ранил, У - убил")
                Action = input("Жду дальнейших указаний: ").upper()
            elif Language == 2:
                print("SHOOTING AT THE POINT {0}{1}".format(Letters[Px],Py))
                print("M - missed, D - Damaged, K - killed")
                Action = input("Waiting for the command: ").upper()
            if Action == "М" or Action == "M":
                if i>1:
                    i=0
                    Sides[Side]=0
                    Side=OpositeSide
                else:
                    i=0
                    Sides[Side]=1
                    Side=0
                Enemy[Py][Px]=1
                PrintField()
                break
            elif Action == "У" or Action == "K":
                Sides=[0,0,0,0,0]
                Enemy[Py][Px]=3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                if Side == 1:
                    Enemy[Py][Px+1] = 1
                    if Enemy[PDy][PDx-1]==0: Enemy[PDy][PDx-1]=1
                elif Side == 2:
                    Enemy[Py+1][Px] = 1
                    if Enemy[PDy-1][PDx]==0: Enemy[PDy-1][PDx]=1
                elif Side == 3:
                    Enemy[Py][Px-1] = 1
                    if Enemy[PDy][PDx+1]==0: Enemy[PDy][PDx+1]=1
                elif Side == 4:
                    Enemy[Py-1][Px] = 1
                    if Enemy[PDy+1][PDx]==0: Enemy[PDy+1][PDx]=1
                Side=0
                PDx=0
                PDy=0
                i=0
                EnemyCount-=1
                PrintField()
                KilledAfterDamage = 1
                break
            elif Action == "Р" or Action == "D":
                Enemy[Py][Px] = 3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                EnemyCount-=1
                if (Side == 1 and (Px+1==21 or Enemy[Py][Px+1]!=0)) or (Side == 2 and (Py+1==21 or Enemy[Py+1][Px]!=0)) or (Side == 3 and (Px-1==0 or Enemy[Py][Px-1]!=0)) or (Side == 4 and (Py-1==0 or Enemy[Py-1][Px]!=0)):
                        Sides[Side]=0
                        Sides[OpositeSide]=1
                        if Side == 1: Px-=i
                        elif Side == 2: Py-=i
                        elif Side == 3: Px+=i
                        elif Side == 4: Py+=i
                        i=0
                        Side=OpositeSide
                PrintField()
            elif Action == "SUICIDE":
                Suicide()     
            elif Action == "KABOOM":
                Kaboom()
            else:
                PrintField()
                print("Неизвестная команда.")
                if Side == 1:
                    Px-=1
                elif Side == 2:
                    Py-=1
                elif Side == 3:
                    Px+=1
                elif Side == 4:
                    Py+=1

def PlayerTurn ():
    global PlayerCount, EnemyCount, Tactic
    while 1:
        if EnemyCount <= 0:
            print("ПОБЕДА")
            if os.name == "nt":
                os.system("pause")
            exit()
        if Tactic == 1:
            while True:
                TacticC = random.randint(1,8)
                if TacticC == 1 or TacticC == 6 or TacticC == 7 or TacticC == 8:
                    Px = random.randint(2,19)
                    Py = random.randint(2,19)
                elif TacticC == 2:
                    Px = 1
                    Py = random.randint(1,20)
                elif TacticC == 3:
                    Px = random.randint(1,20)
                    Py = 1
                elif TacticC == 4:
                    Px = random.randint(1,20)
                    Py = 20
                elif TacticC == 5:
                    Px = 20
                    Py = random.randint(1,20)
                if (Enemy[Py][Px] == 0):
                    break
        elif Tactic == 2:
            while True:
                Px = random.randint(1,20)
                Py = random.randint(1,20)
                if (Enemy[Py][Px] == 0):
                    break
        elif Tactic == 3:
            while True:
                TacticC = random.randint(1,5)
                if TacticC == 1:
                    Px = random.randint(2,19)
                    Py = random.randint(2,19)
                elif TacticC == 2:
                    Px = 1
                    Py = random.randint(1,20)
                elif TacticC == 3:
                    Px = random.randint(1,20)
                    Py = 1
                elif TacticC == 4:
                    Px = random.randint(1,20)
                    Py = 20
                elif TacticC == 5:
                    Px = 20
                    Py = random.randint(1,20)
                if (Enemy[Py][Px] == 0):
                    break

        if Language == 1:
            print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
            print("М - мимо, Р - ранил, У - убил")
            Action = input("Жду дальнейших указаний: ").upper()
        elif Language == 2:
            print("SHOOTING AT THE POINT {0}{1}".format(Letters[Px],Py))
            print("M - missed, D - Damaged, K - killed")
            Action = input("Waiting for the command: ").upper()
        if Action == "М" or Action == "M":
            Enemy[Py][Px] = 1
            PrintField()
            break
        elif Action == "Р" or Action == "D":
            Enemy[Py][Px] = 3
            Enemy[Py-1][Px-1] = 1
            Enemy[Py-1][Px+1] = 1
            Enemy[Py+1][Px+1] = 1
            Enemy[Py+1][Px-1] = 1
            EnemyCount-=1
            PrintField()
            PlayerTurnDamaged(Px,Py)
            break
        elif Action == "У" or Action == "K":
            Enemy[Py][Px] = 3
            Enemy[Py-1][Px-1] = 1
            Enemy[Py-1][Px] = 1
            Enemy[Py-1][Px+1] = 1
            Enemy[Py][Px+1] = 1
            Enemy[Py+1][Px+1] = 1
            Enemy[Py+1][Px] = 1
            Enemy[Py+1][Px-1] = 1
            Enemy[Py][Px-1] = 1
            EnemyCount-=1
            PrintField()
        elif Action == "Т1":
            Tactic = 1
            PrintField()
            print("Выбрана тактика №1")
        elif Action == "Т2":
            Tactic = 2
            PrintField()
            print("Выбрана тактика №2")
        elif Action == "Т3":
            Tactic = 3
            PrintField()
            print("Выбрана тактика №3")
        elif Action == "DEVELOPERMODE":
            DeveloperMode()
        elif Action == "SUICIDE":
            Suicide()
        elif Action == "KABOOM":
            Kaboom()
        else:
            PrintField()
            print("Неизвестная команда.")
    
Player = copy.deepcopy(Enemy)
PrintField()
MapChoose = int(input("Выберите номер карты (1-6, 7 — рандом): "))
if MapChoose == 1:
    Player = Map01
    PrintField()
    print("Выбрана карта \"Костыль и Велосипед\"")
elif MapChoose == 2:
    Player = Map02
    PrintField()
    print("Выбрана карта \"Грязный Гремлин\"")
elif MapChoose == 3:
    Player = Map03
    PrintField()
    print("Выбрана карта \"Вчерашние Сосиски\"")
elif MapChoose == 4:
    Player = Map04
    PrintField()
    print("Выбрана карта \"Ногти самурая\"")
elif MapChoose == 5:
    Player = Map05
    PrintField()
    print("Выбрана карта \"Три Башни\"")
elif MapChoose == 6:
    Player = Map06
    PrintField()
    print("Выбрана карта \"Цветение Сакуры\"")
elif MapChoose == 7:
    Player = RandomMap()
    PrintField()
    print("Выбрана карта \"На всё воля рандома\"")
elif MapChoose == 8:
    PrintField()
    print("Выбрана карта \"Никто не Пришёл\"")
else:
    print("Такой карты нет")
    if os.name == "nt":
        os.system("pause")
    exit()
    
Turn = int(input("Чей первый ход? (1)-игрок (2)-противник: "))
PrintField()
while True:
    if Turn == 1:
        if PlayerCount <= 0:
            print("YOU STINK LOSER")
            break
        if EnemyCount <= 0:
            print("ПОБЕДА")
            break
        if (PDx==0 and PDy==0): 
            PlayerTurn()
        else: PlayerTurnDamaged(PDx,PDy)
        if KilledAfterDamage == 1:
            Turn = 1
            KilledAfterDamage = 0
        else: Turn = 2
    elif Turn == 2:
        if PlayerCount <= 0:
            print("YOU STINK LOSER")
            break
        if EnemyCount <= 0:
            print("ПОБЕДА")
            break
        EnemyTurn()
        Turn = 1
    else:
        if os.name == "nt":
            os.system("pause")
        exit()
