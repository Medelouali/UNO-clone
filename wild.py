import pygame
from utilities.classes.object.Object import Object 
from utilities.classes.object.card import Card
from utilities.classes.object.deck.Deck import Deck
from utilities.classes.Ai.Ai import Ai
from utilities.classes.game.Game import Game    
from utilities.functions.path import getPath
import random

def callback(color):
    def cb():
        Game.getState("lastPlayedCard").setColor(color)
        print(f"you chose {color}")
        Game.check = False
    return cb

green=Object([Game.screenWidth-200, Game.screenHeight-300], [200, 100], getPath("images", "green.png"))
blue=Object([Game.screenWidth-200, Game.screenHeight-400], [200, 100], getPath("images", "blue.png"))
yellow=Object([Game.screenWidth-200, Game.screenHeight-500], [200, 100], getPath("images", "yellow.jpg"))
red=Object([Game.screenWidth-200, Game.screenHeight-600], [200, 100], getPath("images", "red.png"))

def wild ():
    players = Game.getState("playersList")

    if isinstance(players[Game.getState("activePlayer")], Ai) and Game.check:
        print("ai playiiiiing")
        Game.getState("lastPlayedCard").setColor(random.choice(Deck.cardsColors))
        if Game.getState("lastPlayedCard") == 'Red':
            print("red")
            red.add()
            Game.check = False
        elif Game.getState("lastPlayedCard") == 'Green':
            print('green')
            green.add()
            Game.check = False
        elif Game.getState("lastPlayedCard") == 'Yellow':
            print("yellow")
            yellow.add()
            Game.check = False
        elif Game.getState("lastPlayedCard") == 'Blue':
            print("blue")
            blue.add()
            Game.check = False

        print("color set")
    
    else:
        if(Game.check):
            print("human is playing")
            #drawing the buttons on the screen and handling events using callbacks
            red.setCallback(callback('Red')).add()
            blue.setCallback(callback('Blue')).add()
            yellow.setCallback(callback('Yellow')).add()
            green.setCallback(callback('Green')).add()
            
            