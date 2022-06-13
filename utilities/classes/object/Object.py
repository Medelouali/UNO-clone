from turtle import position
import pygame
import utilities.classes.game.Game as Game_t
from utilities.functions.resize import getSize # to avoid circular imports

class Object():
    createdObjects=0 # a unique identifier for each object(id)
    def __init__(self,coordinates=[10, 10], dimensions=[10, 10], icon=None, callback=None):
        #it depends on the object we have each time callback function will have different 
        #implementation
        self.image = pygame.transform.scale(pygame.image.load(icon), getSize(icon, dimensions[0]))
        self.rect=self.image.get_rect()
        self.rect.center=coordinates
        self.coordinates=coordinates
        self.dimensions=dimensions
        self.icon=icon
        self.callback=callback
        self.clicked=False
        #objectId :to differentiate between same object type 
        #the first created object will have an id = 0 and so on 
        self.objectId=Object.createdObjects
        Object.createdObjects+=1
        self.isReactive=True
               
    def update(self):
        pos = pygame.mouse.get_pos()
        #check if the player who touches the mouse is the active one or not
        #if he's not nothing happens
        if(Game_t.Game.getState('activePlayer')!=1):
            return

        if self.rect.collidepoint(pos):  # testing if mouse hovering over Card
             # testing if Card clicked
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked: 
                self.clicked=True
            #depends on the effect of the object (ex :reverse card)
                if(self.callback and self.isReactive):
                    self.callback()
        if(pygame.mouse.get_pressed()[0] == 0):
            self.clicked=False
            
        Game_t.Game.screen.blit(self.image, self.rect)
        self.updateCoord()
        # self.updateDimentions()


    def destroyObject(self):
        if(self.getId() in Game_t.Game.objectsGroup.keys()):
            Game_t.Game.objectsGroup.pop(self.getId())

    # add the created object to the ObjectGroup in order for it to be rendered
    def add(self):
        Game_t.Game.objectsGroup[self.getId()]=self

    #update coordinates of the obj   
    def updateCoord(self):
        Game_t.Game.objectsGroup[self.objectId]=self
    
    #we might need args for the callback function 
    def triggerCallback(self, *args):
        if self.callback:
            if(args):
                self.callback(args)
            else:
                self.callback()
    #setter   
    def setCallback(self, callback):
        self.callback=callback
        
    def generateCallback(self, *args):
        def func():
            self.triggerCallback(*args)
        return func
    
    #getter of the object if    
    def getId(self):
        return self.objectId
    
    def setDimensions(self, dim):
        self.dimensions=dim
        self.image = pygame.transform.scale(pygame.image.load(self.icon), getSize(self.icon, dim[0]))
        return self
    
    # Rect coordinate manipulation and other functions for animations
    def getCoordinates(self):
        return self.rect.center
    
    def setCoordinates(self, to):
        self.rect.center=to
        
    def muteObject(self):
        self.isReactive=False
        return self
        
    def unmuteObject(self):
        self.isReactive=True
        return self