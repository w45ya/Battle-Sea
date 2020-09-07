#Морской Бой v0.6
import os
import random
TestMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,2,2,2,2,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1], [1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
Enemy = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#0 - пустая клетка; 1 - промах, 2 - корабль, 3 - подбитый корабль
PDx = 0
PDy = 0
Side = 0
i = 0

def PrintField (): 
    os.system('clear')
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("                                      _____              ______         _    _    _       ")
    print("              ,:',:`,:',:'           /  ___|             | ___ \       | |  | |  | |      ")
    print("           __||_||_||_||__           \ `--.   ___   __ _ | |_/ /  __ _ | |_ | |_ | |  ___ ")
    print("      ____[\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"]____       `--. \ / _ \ / _` || ___ \ / _` || __|| __|| | / _ \\")
    print("      \ \" '''''''''''''''''''' |     /\__/ /|  __/| (_| || |_/ /| (_| || |_ | |_ | ||  __/  indev v0.6")
    print("    ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^   \____/  \___| \__,_|\____/  \__,_| \__| \__||_| \___|  it just works!")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("  | 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20  ||    | 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20")
    print("--|------------------------------------------------------------  ||  --|------------------------------------------------------------")
    for i in range (1,21): 
        print("{:02d}".format(i),end="")
        print("| ",end="")
        for j in range (1,21): 
            if Player[i][j] == 0:
                print("~",end = "  ")
            if Player[i][j] == 1:
                print("#",end = "  ")
            if Player[i][j] == 2:
                print("О",end = "  ")
            if Player[i][j] == 3:
                print("Х",end = "  ")
            #print ( "{:3d}".format(Player[i][j]), end = "" )
        print (" ||  ", end = "" )
        print("{:02d}".format(i),end="")
        print("| ",end="")
        for j in range (1,21): 
            if Enemy[i][j] == 0:
                print("~",end = "  ")
            if Enemy[i][j] == 1:
                print("#",end = "  ")
            if Enemy[i][j] == 2:
                print("О",end = "  ")
            if Enemy[i][j] == 3:
                print("Х",end = "  ")
            #print ( "{:3d}".format(Enemy[i][j]), end = "" ) 
        print ()
        
def EnemyTurn ():
    print("Ход противника.")
    Ex = int(input("Введите первую координату: "))
    Ey = int(input("Введите вторую координату: "))
    if Player[Ey][Ex]==2:
        Player[Ey][Ex]=3
        PrintField()
        print("ПОПАЛ")
        EnemyTurn()
    else:
        Player[int(Ey)][int(Ex)]=1
        PrintField()
        print("ПРОМАЗАЛ")

def PlayerTurnDamaged (Px,Py):
    PrintField()
    global PDx, PDy, Side, i
    if PDx==0: PDx=Px
    if PDy==0: PDy=Py
    if Side==0: Side=random.randint(1,4)
    i+=1
    if Side==1:
        if (Enemy[Py][Px+1]!=0 & Px+1!=21): 
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
        Px+=1 
        print("СТРЕЛЯЮ ПО ТОЧКЕ {0},{1}".format(Px,Py))
        print("m - промах, d - ранил, k - убил")
        Action = input("Жду дальнейших указаний: ")
        if Action == "m":
            if i>1:
                i=0
                Side=3
            else:
                i=0
                Side=0
            Enemy[Py][Px]=1
            PrintField()
        elif Action == "k":
            Side=0
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
            PrintField()
            PlayerTurn()
        elif Action == "d":
            Enemy[Py][Px] = 3
            Enemy[Py-1][Px-1] = 1
            Enemy[Py-1][Px+1] = 1
            Enemy[Py+1][Px+1] = 1
            Enemy[Py+1][Px-1] = 1
            if Px+1==21:
                i=0
                Side=3
                PlayerTurnDamaged(PDx,PDy)
            else: PlayerTurnDamaged(Px,Py)
        elif Action == "F":
            for i in range (1,21): 
                for j in range (1,21):
                    if Player[i][j]==2:
                        Player[i][j]=3
            PrintField()
            print("PAYING RESPECT")
            exit() 
        elif Action == "KABOOM":
            for i in range (1,21): 
                for j in range (1,21):
                    Enemy[i][j]=3
            PrintField()
            exit() 
            
    elif Side==2:
        if (Enemy[Py+1][Px]!=0 & Py+1!=21): 
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
        Py+=1 
        print("СТРЕЛЯЮ ПО ТОЧКЕ {0},{1}".format(Px,Py))
        print("m - промах, d - ранил, k - убил")
        Action = input("Жду дальнейших указаний: ")
        if Action == "m":
            if i>1:
                i=0
                Side=4
            else:
                i=0
                Side=0
            Enemy[Py][Px]=1
            PrintField()
        elif Action == "k":
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
            PrintField()
            PlayerTurn()
        elif Action == "d":
            Enemy[Py][Px] = 3
            Enemy[Py-1][Px-1] = 1
            Enemy[Py-1][Px+1] = 1
            Enemy[Py+1][Px+1] = 1
            Enemy[Py+1][Px-1] = 1
            if Py+1==0:
                i=0
                Side=4
                PlayerTurnDamaged(PDx,PDy)
            else: PlayerTurnDamaged(Px,Py)
        elif Action == "F":
            for i in range (1,21): 
                for j in range (1,21):
                    if Player[i][j]==2:
                        Player[i][j]=3
            PrintField()
            print("PAYING RESPECT")
            exit() 
        elif Action == "KABOOM":
            for i in range (1,21): 
                for j in range (1,21):
                    Enemy[i][j]=3
            PrintField()
            exit()          
            
    elif Side==3:
        if (Enemy[Py][Px-1]!=0 & Px-1!=0): 
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
        Px-=1 
        print("СТРЕЛЯЮ ПО ТОЧКЕ {0},{1}".format(Px,Py))
        print("m - промах, d - ранил, k - убил")
        Action = input("Жду дальнейших указаний: ")
        if Action == "m":
            if i>1:
                i=0
                Side=1
            else:
                i=0
                Side=0
            Enemy[Py][Px]=1
            PrintField()
        elif Action == "k":
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
            PrintField()
            PlayerTurn()
        elif Action == "d":
            Enemy[Py][Px] = 3
            Enemy[Py-1][Px-1] = 1
            Enemy[Py-1][Px+1] = 1
            Enemy[Py+1][Px+1] = 1
            Enemy[Py+1][Px-1] = 1
            if Px-1==0:
                i=0
                Side=1
                PlayerTurnDamaged(PDx,PDy)
            else: PlayerTurnDamaged(Px,Py)
        elif Action == "F":
            for i in range (1,21): 
                for j in range (1,21):
                    if Player[i][j]==2:
                        Player[i][j]=3
            PrintField()
            print("PAYING RESPECT")
            exit() 
        elif Action == "KABOOM":
            for i in range (1,21): 
                for j in range (1,21):
                    Enemy[i][j]=3
            PrintField()
            exit() 
            
    elif Side==4:
        if (Enemy[Py-1][Px]!=0 & Py-1!=0): 
            Side = 0
            PlayerTurnDamaged(PDx,PDy)
        Py-=1 
        print("СТРЕЛЯЮ ПО ТОЧКЕ {0},{1}".format(Px,Py))
        print("m - промах, d - ранил, k - убил")
        Action = input("Жду дальнейших указаний: ")
        if Action == "m":
            if i>1:
                i=0
                Side=2
            else:
                i=0
                Side=0
            Enemy[Py][Px]=1
            PrintField()
        elif Action == "k":
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
            PrintField()
            PlayerTurn()
        elif Action == "d":
            Enemy[Py][Px] = 3
            Enemy[Py-1][Px-1] = 1
            Enemy[Py-1][Px+1] = 1
            Enemy[Py+1][Px+1] = 1
            Enemy[Py+1][Px-1] = 1
            if Py-1==0:
                i=0
                Side=2
                PlayerTurnDamaged(PDx,PDy)
            else: PlayerTurnDamaged(Px,Py)
        elif Action == "F":
            for i in range (1,21): 
                for j in range (1,21):
                    if Player[i][j]==2:
                        Player[i][j]=3
            PrintField()
            print("PAYING RESPECT")
            exit() 
        elif Action == "KABOOM":
            for i in range (1,21): 
                for j in range (1,21):
                    Enemy[i][j]=3
            PrintField()
            exit()         
            
def PlayerTurn ():
    #Px = int(input("Введите первую координату: "))
    #Py = int(input("Введите вторую координату: "))
    Px = random.randint(1,20)
    Py = random.randint(1,20)
    if Enemy[Py][Px] != 0:
        PlayerTurn()
    if Enemy[Py][Px] != 0:
        PlayerTurn()
    if Enemy[Py][Px] != 0:
        PlayerTurn()
    print("СТРЕЛЯЮ ПО ТОЧКЕ {0},{1}".format(Px,Py))
    print("m - промах, d - ранил, k - убил")
    Action = input("Жду дальнейших указаний: ")
    if Action == "m":
        Enemy[Py][Px] = 1
        PrintField()
    elif Action == "d":
        Enemy[Py][Px] = 3
        Enemy[Py-1][Px-1] = 1
        Enemy[Py-1][Px+1] = 1
        Enemy[Py+1][Px+1] = 1
        Enemy[Py+1][Px-1] = 1
        PlayerTurnDamaged(Px,Py)
    elif Action == "k":
        Enemy[Py][Px] = 3
        Enemy[Py-1][Px-1] = 1
        Enemy[Py-1][Px] = 1
        Enemy[Py-1][Px+1] = 1
        Enemy[Py][Px+1] = 1
        Enemy[Py+1][Px+1] = 1
        Enemy[Py+1][Px] = 1
        Enemy[Py+1][Px-1] = 1
        Enemy[Py][Px-1] = 1
        PrintField()
        PlayerTurn()
    elif Action == "F":
        for i in range (1,21): 
            for j in range (1,21):
                if Player[i][j]==2:
                    Player[i][j]=3
        PrintField()
        print("PAYING RESPECT")
        exit() 
    elif Action == "KABOOM":
        for i in range (1,21): 
            for j in range (1,21):
                Enemy[i][j]=3
        PrintField()
        exit() 
    else:
        PrintField()
        print("Неизвестная команда.")
        PlayerTurn()
        
Player = TestMap
PrintField()
#EnemyTurn()
while (1==1):
    if (PDx==0 & PDy==0): 
        PlayerTurn()
    else: PlayerTurnDamaged(PDx,PDy)    
#Дописать: карты, выбор карты, выбор первенства, эндгейм
#Тестировать и править баги
#Если будет время: Присобачить графику, усовершенствовать алгоритм, мелкие фичи just for lulz
