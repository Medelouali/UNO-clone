import pygame
import utilities.classes.game.Game as Game_t # to avoid circular imports

class Object():
    gaps=0 # the number of destroyed of objects, it helps for insertion
    createdObjects=0
    def __init__(self, isVisible=False, coordinates=[10, 10], dimensions=[10, 10], icon=None):
        # pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(icon)
        self.rect=self.image.get_rect()
        self.rect.center=coordinates
        self.isVisible=isVisible
        self.dimensions=dimensions
        # canMove will be used to test if we can drag the object with the mouse or not
        # it'll be False by default but here it's True just for testing purposes
        self.camMove=True
        self.clicked=False
        self.objectId=Object.createdObjects
        Object.createdObjects+=1
        
    def update(self):
        event= Game_t.Game.getState(Game_t.Game, 'event')
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):  # testing if mouse hovering over Card
            if pygame.mouse.get_pressed()[0] == 1 and self.camMove:  # testing if Card clicked
                if event.type ==  pygame.MOUSEMOTION:  # testing if mouse moving
                    self.rect.move_ip(event.rel)
                    
        Game_t.Game.screen.blit(self.image, self.rect)
        self.updateCoord()
                
    def fixIt(self):
        self.camMove=False
    
    def makeItMovable(self):
        self.camMove=True
        
    def destroyObject(self):
        # this is more efficient than deleting an item of a list
        # and shiffting the items around! 
        Game_t.Game.objectsGroup[self.objectId]=None
        Object.gaps+=1 
        
    def add(self):
        len_t=len(Game_t.Game.objectsGroup)
        if(self.gaps>0):
            for i in range(len_t):
                if(not Game_t.Game.objectsGroup[i]):
                    Game_t.Game.objectsGroup[i]=self
                    break
        else:
            Game_t.Game.objectsGroup.append(self)
        
    def updateCoord(self):
        Game_t.Game.objectsGroup[self.objectId]=self
    