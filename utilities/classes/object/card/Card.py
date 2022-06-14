import numbers
import time
from utilities.classes.Ai.random_ai import random_ai
from utilities.classes.Ai.bot_player import bot_player
from utilities.classes.Ai.advanced_ai import advanced_ai
# from utilities.classes.game.Game import Game
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath

from utilities.classes.object.color_picker import ColorPicker
import pygame

class Card(Object):
    def __init__(self, number=None, color=None, type="Normal", coordinates=[1, 1], 
                dimensions=[100, 100], icon=getPath("images", "logo.png"), callback=None, ownerId=None):
        super().__init__(coordinates, dimensions, icon, callback=lambda : self.throwCard(1))
        #callback=lambda : self.throwCard(1) : when we click the card it must be played
        self.number = number
        self.color=color
        self.type=type
        self.icon = icon
        # to know who throwed the card
        self.ownerId=ownerId
        self.played=False
        self.start_time=pygame.time.get_ticks()
        
    # coloredType=["Skip", "Reverse", "Draw 2", "Draw 4", "Wild"]
    # get card's type 
    def getCardType(self):
        return self.type
    # set card's color
    def setCardColor(self,color):
        self.color = color
    # if a card is played this method returns True
    def isPlayed(self):
        return self.played
    # set played attr to True when a card is played
    def setPlayed(self):
        self.played = True
    # to get position of a card 
    def getPosition(self):
        return self.rect.center
    # to set new position of a card
    def setPosition(self, coordinates):
        self.rect.center = coordinates
    #we need this return value to add the ( ex card) to the ObjGrp        
        return self # We need this return value to chain methods
    
    # to get icon from a card
    def getIcon(self):
        return self.icon
    #getter for dimensions
    def getDimensions(self):
        return self.dimensions


    def compareSingleCard(self):
        from utilities.classes.game.Game import Game as Game_t
        lastPlayedCard=Game_t.state["lastPlayedCard"]
        #if this the first card on the game nothing happens 
        if(not lastPlayedCard):
            return self
        #for wild card
        if self.type=="Wild":
                return self
        if(lastPlayedCard.type=="Wild"):
                if(Game_t.state["chosen_color"]==self.getColor()):
                    # in case you played a card after a wild one , the color should be returned to None
                    Game_t.colorPicker.resetPickedColor()
                    return self
        if self.type=="Normal":
            if(lastPlayedCard.getColor()==self.getColor() or lastPlayedCard.getNumber()==self.getNumber()):
                return self
        #if it's a special card
        elif self.type in ["Skip", "Reverse", "Draw", "Draw4"]:
            if(lastPlayedCard.getColor()==self.getColor()):
                return self
        return None
    
    def throwCard(self, playerId):
        from utilities.classes.game.Game import Game as Game_t
        pygame.time.delay(1000)
    #we need the playerId in case not the activePlayer
        if playerId==Game_t.state["activePlayer"]:
            #if compareSingleCard() returns a card
            if self.compareSingleCard():
                newHand=[]
                #we want to know which cards will be in the new hand
                for card in Game_t.getState("playersList")[playerId].getHand():
                    if(card.getId()!=self.getId()):
                        newHand.append(card)
                #the nexPlayer is the same activePlayer but we want to update his hand 
                newPlayer=Game_t.getState("playersList")[playerId]
                newPlayer.hand=newHand
                Game_t.state["playersList"][playerId]=newPlayer
                Game_t.playedCards[self.getId()]=self
                Game_t.state["lastPlayedCard"]=self
                self.applyEffect()
                # Only rotate if it's not wild card 
                # In case it's a wild card , rotation whill happen only when player picks a color
                if(Game_t.getState("lastPlayedCard").getCardType()!="Wild"):
                    Game_t.rotate()
                    self.handleMessage()
                # Game_t.colorPicker.resetPickedColor()
                Game_t.setState("timer",10)
                return True
    # to apply last played card special effect 
    def applyEffect(self): 
        from utilities.classes.game.Game import Game as Game
        if(self.getCardType() != "Normal"):
                Game.getState("lastPlayedCard").setPlayed()
                if(Game.getState("lastPlayedCard").getCardType()=="Draw"):
                    print("Next player draws 2")
                    Game.deck.draw(2,(Game.getState("activePlayer")+1)%2)
                    Game.rotate()
                elif(Game.getState("lastPlayedCard").getCardType()=="Draw4"):
                    print("Next player draws 4")
                    Game.deck.draw(4,(Game.getState("activePlayer")+1)%2)
                    Game.rotate()
                elif(Game.getState("lastPlayedCard").getCardType()=="Reverse"):
                    print("Reverse order")
                    Game.rotate()
                elif(Game.getState("lastPlayedCard").getCardType()=="Skip"):
                    print("Skip to next player")
                    Game.rotate()
                elif(Game.getState("lastPlayedCard").getCardType()=="Wild"):
                    if(isinstance(Game.getState("playersList")[Game.getState("activePlayer")], bot_player)):
                        current_player = Game.getState("playersList")[Game.getState("activePlayer")]
                        color = current_player.getCommonColor(range(len(current_player.getHand())))
                        Game.setState("chosen_color",color.capitalize())
                        Game.setState("message", f"I chose {color.capitalize()}")
                    else:
                        Game.colorPicker.fillColors()
                        Game.colorPicker.drawColors()
        
    def handleMessage(self):
        from utilities.classes.game.Game import Game as Game_t
        if self.type in ["Skip", "Reverse", "Draw", "Draw4"]:
            Game_t.setState("message", f"Woow! {self.getPlayerName()} played {self.type} card!")
            return
        if(Game_t.getState("lastPlayedCard").getCardType()=="Wild"):
            Game_t.setState("message", f"Niice {self.getPlayerName()} played wild card!")
            return
        if(Game_t.getState("lastPlayedCard").getCardType()=="Normal"):
            color=Game_t.getState("lastPlayedCard").getColor()
            number=Game_t.getState("lastPlayedCard").getNumber()
            Game_t.setState("message", f"{self.getPlayerName()} played {number} with {color} color!")
            return
        Game_t.setState("message", "")
    def getColor(self):
        return self.color
    
    def getNumber(self):
        return self.number
    def __str__(self):
        return f"Number : {self.number} Color : {self.color}"
    
    def getPlayerName(self):
        from utilities.classes.game.Game import Game as Game_t
        if(Game_t.getState("activePlayer")):
            return "Bot"
        return "You"
    
    