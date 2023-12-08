import pygame
from src.Constants import Constants as C
class Monkey(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        #corrects to center over tile
        self.tile_x = pos[0] // C.TILESIZE
        self.tile_y = pos[1] // C.TILESIZE
        self.x = (self.tile_x +.5) * C.TILESIZE
        self.y = (self.tile_y +.5) * C.TILESIZE
        
        #loads and scales image 
        self.image = pygame.image.load(image)
        self.image= pygame.transform.scale(self.image,(C.TILESIZE,C.TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.center = ((self.x,self.y))
