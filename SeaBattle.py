#Морской Бой v0.9.8
import os
import random
import time
from termcolor import colored
Map01 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,2,0,2,0,0,0,0,0,2,2,0,2,2,0,2,2,0,0,1], [1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,0,2,2,0,0,0,0,2,2,0,2,2,0,2,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map02 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,2,0,2,0,0,0,0,0,2,2,0,2,2,0,2,2,0,0,1], [1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,0,2,2,0,0,0,0,2,2,0,2,2,0,2,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map03 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,2,0,2,0,0,0,0,0,2,2,0,2,2,0,2,2,0,0,1], [1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,0,2,2,0,0,0,0,2,2,0,2,2,0,2,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map04 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,2,0,2,0,0,0,0,0,2,2,0,2,2,0,2,2,0,0,1], [1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,0,2,2,0,0,0,0,2,2,0,2,2,0,2,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map05 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,1], [1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,2,0,2,0,0,0,0,0,2,2,0,2,2,0,2,2,0,0,1], [1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,0,2,2,0,0,0,0,2,2,0,2,2,0,2,2,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,2,2,0,2,2,2,0,0,2,2,2,0,0,2,2,2,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1], [1,0,0,0,0,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Map06 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Enemy = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#0 - пустая клетка; 1 - промах, 2 - корабль, 3 - подбитый корабль
PDx = 0
PDy = 0
Side = 0
i = 0
PlayerCount = 76
EnemyCount = 76
Letters = "ЁАБВГДЕЖЗИКЛМНОПРСТУФЙ"
Sides=[0,0,0,0,0]

def PrintField (): 
    os.system('clear')
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print(colored("                                      _____              ______         _    _    _                                                  ",'red','on_blue',attrs=['bold']))
    print(colored("              ,:',:`,:',:'          ",'white','on_blue',attrs=['bold'])+colored(" /  ___|             | ___ \       | |  | |  | |                                                 ",'red','on_blue',attrs=['bold']))
    print(colored("           __||_||_||_||__          ",'red','on_blue')+colored(" \ `--.   ___   __ _ | |_/ /  __ _ | |_ | |_ | |  ___                                            ",'red','on_blue',attrs=['bold']))
    print(colored("      ____[\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"]____     ",'red','on_blue',attrs=['bold'])+colored("  `--. \ / _ \ / _` || ___ \ / _` || __|| __|| | / _ \\                                           ",'red','on_blue',attrs=['bold']))
    print(colored("      \ \" '''''''''''''''''''' |    ",'red','on_blue',attrs=['bold'])+colored(" /\__/ /|  __/| (_| || |_/ /| (_| || |_ | |_ | ||  __/ ",'red','on_blue',attrs=['bold'])+colored("  indev v0.9.8                            ",'green','on_blue',attrs=['bold']))
    print(colored("    ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^  ",'blue','on_blue',attrs=['bold'])+colored(" \____/  \___| \__,_|\____/  \__,_| \__| \__||_| \___| ",'red','on_blue',attrs=['bold'])+colored("  it just works!                          ",'green','on_blue',attrs=['bold']))
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("--|-----------------------------","{:02d}".format(PlayerCount),"---------------------------  ||  --|-----------------------------","{:02d}".format(EnemyCount),"-----------------------------")
    print("--|------------------------------------------------------------  ||  --|-------------------------------------------------------------")
    print("  |  А  Б  В  Г  Д  Е  Ж  З  И  К  Л  М  Н  О  П  Р  С  Т  У  Ф  ||    |  А  Б  В  Г  Д  Е  Ж  З  И  К  Л  М  Н  О  П  Р  С  Т  У  Ф ")
    #print("  | 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20  ||    | 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20")
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
            #print ( "{:3d}".format(Player[i][j]), end = "" )
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
            #print ( "{:3d}".format(Enemy[i][j]), end = "" ) 
        print ()
        
def EnemyTurn ():
    global PlayerCount, EnemyCount
    if PlayerCount <= 0:
        print("YOU STINK LOSER")
        exit()
    print("Ход противника.")
    Et = input("Введите координаты: ")
    try:
        for i in range(len(Letters)): 
            if (Et[0]==Letters[i]): Ex = i
    
        if len(Et) == 2:
            Ey = int(Et[1])
        else:
            Ey = int(Et[1])*10+int(Et[2])
    except:
        print("Неверная координата")
        EnemyTurn()
    else:
        if Player[Ey][Ex]==2:
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

def PlayerTurnDamaged (Px,Py):
    PrintField()
    global PDx, PDy, Side, i, PlayerCount, EnemyCount, Sides
    if EnemyCount <= 0:
        print("ПОБЕДА")
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
    if Side==1:
        Sides[Side]==1
        if (Enemy[Py][Px+1]!=0 and Px+1==21): 
            Sides[Side]=0
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
            return
        else:
            Px+=1 
            print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
            print("М - мимо, Р - ранил, У - убил")
            Action = input("Жду дальнейших указаний: ")
            if Action == "М":
                if i>1:
                    i=0
                    Sides[Side]=0
                    Side=3
                else:
                    i=0
                    Sides[Side]=1
                    Side=0
                Enemy[Py][Px]=1
                PrintField()
                return
            elif Action == "У":
                Side=0
                Sides=[0,0,0,0,0]
                Enemy[Py][Px]=3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                Enemy[Py][Px+1] = 1
                if Enemy[PDy][PDx-1]==0: Enemy[PDy][PDx-1]=1
                PDx=0
                PDy=0
                i=0
                EnemyCount-=1
                PrintField()
                PlayerTurn()
            elif Action == "Р":
                Enemy[Py][Px] = 3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                EnemyCount-=1
                if Px+1==21 or Enemy[Py][Px+1]!=0:
                    i=0
                    Sides[Side]=0
                    Side=3
                    PlayerTurnDamaged(PDx,PDy)
                else: PlayerTurnDamaged(Px,Py)
            elif Action == "F":
                for i in range (1,21): 
                    for j in range (1,21):
                        if Player[i][j]==2:
                            Player[i][j]=3
                PrintField()
                PlayerCount=0
                print("paying respect...")
                exit()
    
            elif Action == "KABOOM":
                for i in range (1,21): 
                    for j in range (1,21):
                        Enemy[i][j]=3
                PrintField()
                EnemyCount=0
                print("what a mess we made...")
                exit()
            else:
                PrintField()
                print("Неизвестная команда.")
                PlayerTurnDamaged(Px-1,Py)
            
    elif Side==2:
        Sides[Side]==1
        if (Enemy[Py+1][Px]!=0 and Py+1==21): 
            Sides[Side]=0
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
            return
        else:
            Py+=1 
            print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
            print("М - мимо, Р - ранил, У - убил")
            Action = input("Жду дальнейших указаний: ")
            if Action == "М":
                if i>1:
                    i=0
                    Sides[Side]=0
                    Side=4
                else:
                    i=0
                    Sides[Side]=1
                    Side=0
                Enemy[Py][Px]=1
                PrintField()
                return
            elif Action == "У":
                Sides=[0,0,0,0,0]
                Side=0
                Enemy[Py][Px]=3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                Enemy[Py+1][Px] = 1
                if Enemy[PDy-1][PDx]==0: Enemy[PDy-1][PDx]=1
                PDx=0
                PDy=0
                i=0
                EnemyCount-=1
                PrintField()
                PlayerTurn()
            elif Action == "Р":
                Enemy[Py][Px] = 3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                EnemyCount-=1
                if Py+1==0 or Enemy[Py+1][Px]!=0:
                    i=0
                    Sides[Side]=0
                    Side=4
                    PlayerTurnDamaged(PDx,PDy)
                else: PlayerTurnDamaged(Px,Py)
            elif Action == "F":
                for i in range (1,21): 
                    for j in range (1,21):
                        if Player[i][j]==2:
                            Player[i][j]=3
                PrintField()
                PlayerCount=0
                print("paying respect...")
                exit()
            elif Action == "KABOOM":
                for i in range (1,21): 
                    for j in range (1,21):
                        Enemy[i][j]=3
                PrintField()
                EnemyCount=0
                print("what a mess we made...")
                exit()
            else:
                PrintField()
                print("Неизвестная команда.")
                PlayerTurnDamaged(Px,Py-1)
                
    elif Side==3:
        Sides[Side]==1
        if (Enemy[Py][Px-1]!=0 and Px-1==0): 
            Sides[Side]=0
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
            return
        else:
            Px-=1 
            print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
            print("М - мимо, Р - ранил, У - убил")
            Action = input("Жду дальнейших указаний: ")
            if Action == "М":
                if i>1:
                    i=0
                    Sides[Side]=0
                    Side=1
                else:
                    i=0
                    Sides[Side]=1
                    Side=0
                Enemy[Py][Px]=1
                PrintField()
                return
            elif Action == "У":
                Sides=[0,0,0,0,0]
                Side=0
                Enemy[Py][Px]=3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                Enemy[Py][Px-1] = 1
                if Enemy[PDy][PDx+1]==0: Enemy[PDy][PDx+1]=1
                PDx=0
                PDy=0
                i=0
                EnemyCount-=1
                PrintField()
                PlayerTurn()
            elif Action == "Р":
                Enemy[Py][Px] = 3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                EnemyCount-=1
                if Px-1==0 or Enemy[Py][Px-1]!=0:
                    i=0
                    Sides[Side]=0
                    Side=1
                    PlayerTurnDamaged(PDx,PDy)
                else: PlayerTurnDamaged(Px,Py)
            elif Action == "F":
                for i in range (1,21): 
                    for j in range (1,21):
                        if Player[i][j]==2:
                            Player[i][j]=3
                PrintField()
                PlayerCount=0
                print("paying respect...")
                exit()
            elif Action == "KABOOM":
                for i in range (1,21): 
                    for j in range (1,21):
                        Enemy[i][j]=3
                PrintField()
                EnemyCount=0
                print("what a mess we made...")
                exit()
            else:
                PrintField()
                print("Неизвестная команда.")
                PlayerTurnDamaged(Px+1,Py)
                
    elif Side==4:
        Sides[Side]==1
        if (Enemy[Py-1][Px]!=0 and Py-1==0):
            Sides[Side]=0
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
            return
        else:
            Py-=1 
            print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
            print("М - мимо, Р - ранил, У - убил")
            Action = input("Жду дальнейших указаний: ")
            if Action == "М":
                if i>1:
                    i=0
                    Sides[Side]=0
                    Side=2
                else:
                    i=0
                    Sides[Side]=1
                    Side=0
                Enemy[Py][Px]=1
                PrintField()
                return
            elif Action == "У":
                Sides=[0,0,0,0,0]
                Side=0
                Enemy[Py][Px]=3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                Enemy[Py-1][Px] = 1
                if Enemy[PDy+1][PDx]==0: Enemy[PDy+1][PDx]=1
                PDx=0
                PDy=0
                i=0
                EnemyCount-=1
                PrintField()
                PlayerTurn()
            elif Action == "Р":
                Enemy[Py][Px] = 3
                Enemy[Py-1][Px-1] = 1
                Enemy[Py-1][Px+1] = 1
                Enemy[Py+1][Px+1] = 1
                Enemy[Py+1][Px-1] = 1
                EnemyCount-=1
                if Py-1==0 or Enemy[Py-1][Px]!=0:
                    i=0
                    Sides[Side]=0
                    Side=2
                    PlayerTurnDamaged(PDx,PDy)
                else: PlayerTurnDamaged(Px,Py)
            elif Action == "F":
                for i in range (1,21): 
                    for j in range (1,21):
                        if Player[i][j]==2:
                            Player[i][j]=3
                PrintField()
                PlayerCount=0
                print("paying respect...")
                exit()
            elif Action == "KABOOM":
                for i in range (1,21): 
                    for j in range (1,21):
                        Enemy[i][j]=3
                PrintField()
                EnemyCount=0
                print("what a mess we made...")
                exit()
            else:
                PrintField()
                print("Неизвестная команда.")
                PlayerTurnDamaged(Px,Py+1)

def PlayerTurn ():
    global PlayerCount, EnemyCount
    if EnemyCount <= 0:
        print("ПОБЕДА")
        exit()
    #Px = int(input("Введите первую координату: "))
    #Py = int(input("Введите вторую координату: "))
    Tactic = 1
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
            Px = random.randint(2,19)
            Py = random.randint(2,19)
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
    print("СТРЕЛЯЮ ПО ТОЧКЕ {0}{1}".format(Letters[Px],Py))
    print("М - мимо Р - ранил, У - убил")
    Action = input("Жду дальнейших указаний: ")
    if Action == "М":
        Enemy[Py][Px] = 1
        PrintField()
        return
    elif Action == "Р":
        Enemy[Py][Px] = 3
        Enemy[Py-1][Px-1] = 1
        Enemy[Py-1][Px+1] = 1
        Enemy[Py+1][Px+1] = 1
        Enemy[Py+1][Px-1] = 1
        EnemyCount-=1
        PlayerTurnDamaged(Px,Py)
    elif Action == "У":
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
        PlayerTurn()
    elif Action == "Т1":
        Tactic = 1
        PrintField()
        print("Выбрана тактика №1")
        PlayerTurn()
    elif Action == "Т2":
        Tactic = 2
        PrintField()
        print("Выбрана тактика №2")
        PlayerTurn()
    elif Action == "Т3":
        Tactic = 3
        PrintField()
        print("Выбрана тактика №3")
        PlayerTurn()
    elif Action == "F":
        for i in range (1,21): 
            for j in range (1,21):
                if Player[i][j]==2:
                    Player[i][j]=3
        PrintField()
        PlayerCount=0
        print("paying respect...")
        exit()
    elif Action == "KABOOM":
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
        exit()
    else:
        PrintField()
        print("Неизвестная команда.")
        PlayerTurn()
        
Player = Enemy
PrintField()

MapChoose = int(input("Выберите номер карты (1-6): "))
if MapChoose == 1:
    Player = Map01
elif MapChoose == 2:
    Player = Map02
elif MapChoose == 3:
    Player = Map03
elif MapChoose == 4:
    Player = Map04
elif MapChoose == 5:
    Player = Map05
elif MapChoose == 6:
    Player = Map06
PrintField()

Turn = int(input("Чей первый ход? (1)-игрок (2)-противник: "))

while PlayerCount > 0 and EnemyCount > 0:
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
        Turn = 2
    elif Turn == 2:
        if PlayerCount <= 0:
            print("YOU STINK LOSER")
            break
        if EnemyCount <= 0:
            print("ПОБЕДА")
            break
        EnemyTurn()
        Turn = 1

#Дописать: карты
#Тестировать и править баги 
#Если будет время: Тактики, мелкие фичи just for lulz
