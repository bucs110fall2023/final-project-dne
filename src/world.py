import pygame
from src.Constants import Constants as C
class World():
    #loads image 
    def __init__(self,map_image):
        self.image = pygame.image.load(map_image)
    #blits and redraws screen
    def draw(self,surface,cords=(0,0)):
        surface.blit(self.image,cords)