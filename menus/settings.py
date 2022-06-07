import pygame,sys
from menus.functions import draw_text
from menus.functions import font
from menus.functions import screen   #screenWidth=1280    screenHeight=640
from utilities.classes.game.Game import Game

pygame.init()

def SettingsMenu(ActMenu,RectDic):
    Q=True#Loop's variable
    Backbutton=(600 ,500)
    Difficult=(1100 ,100)
    NumPlayers=(250 ,100)
    NumScreen=(250,300)
    Num=Game.getState("numOfPlayers")
    Diff=Game.getState("difficulty")
    DiffScreen=(1100,300)
    #Positive and negative button needed variables
    PosButton =pygame.transform.scale(pygame.image.load("assets/images/Buttons/PlusButton.png"),(30,30))
    PosRect = PosButton.get_rect()
    PosRect.center= ( 400 ,300)
    RectDic["Pos"]= PosRect
    MinButton =pygame.transform.scale(pygame.image.load("assets/images/Buttons/MinusButton.png"),(30,30))
    MinRect = MinButton.get_rect()
    MinRect.center = (100,300)
    RectDic["Min"]= MinRect

    while(Q):

        for event in pygame.event.get():
        # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            # check mouse click
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                if( RectDic["Back"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="SettingsMenu"):
                    print ("Back")
                    Game.setState("numOfPlayers",Num)
                    Game.setState("difficulty",Diff)
                    Q=False
                if( RectDic["Difficulty"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="SettingsMenu" ):
                    print ("changing difficulty")
                if( RectDic["Number of players"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="SettingsMenu" ):
                    print ("changing the number of players")
                if( RectDic["Pos"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="SettingsMenu" ):
                    print("ADD")
                    if (Num<4): 
                        Num+=1
                if( RectDic["Min"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="SettingsMenu" ):
                    print ("DELETE")
                    if (Num>2): Num-=1
                if( RectDic[Diff].collidepoint(pygame.mouse.get_pos()) and ActMenu=="SettingsMenu"):
                    if(Diff=="Normal"):
                        print("changing to Hard")
                        Diff="Hard"
                    else:
                        print("changing to Normal")
                        Diff="Normal"

        
        #Screen blit and updating                
        screen.fill((160,160,160))
        draw_text("Difficulty",font,(255 ,255 ,255),screen,Difficult,RectDic)
        draw_text("Number of players",font,(255 ,255 ,255),screen,NumPlayers,RectDic)
        draw_text("Back",font,(255 ,255 ,255),screen,Backbutton,RectDic)
        draw_text(str(Num),font,(255 ,255 ,255),screen,NumScreen,RectDic)
        draw_text(Diff,font,(255 ,255 ,255),screen,DiffScreen,RectDic)
        screen.blit(PosButton ,PosRect)
        screen.blit(MinButton ,MinRect)
        pygame.display.update()