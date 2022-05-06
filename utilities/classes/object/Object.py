import pygame
import utilities.classes.game.Game as Game_t # to avoid circular imports

class Object(pygame.sprite.Sprite):
    def __init__(self, isVisible=False, coordinates=[10, 10], icon=None):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(icon)
        self.rect=self.image.get_rect()
        self.rect.center=coordinates
        self.rect.x=coordinates[0]
        self.rect.y=coordinates[1]
        self.isVisible=isVisible
        self.coordinates=coordinates
        self.icon=icon
        # canMove will be used to test if we can drag the object with the mouse or not
        # it'll be False by default but here it's True just for testing purposes
        self.camMove=True
        
    def update(self):
        event= Game_t.Game.getState(Game_t.Game, 'event')
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):  # testing if mouse hovering over Card
            if pygame.mouse.get_pressed()[0] == 1:  # testing if Card clicked
                if event.type == pygame.MOUSEMOTION and self.camMove:  # testing if mouse moving
                    self.rect.center=pos
                
    def fixIt(self):
        self.camMove=False
    
    def makeItMovable(self):
        self.camMove=True
        
    def destroyObject(self):
        # Will be implemented soon
        print("Object is gone")