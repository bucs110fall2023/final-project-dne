import pygame


class World():
    #loads image 
    def __init__(self,map_image):
        self.image = pygame.image.load(map_image)
    #blits and redraws screen
    def draw(self,surface):
        surface.blit(self.image,(0,0))
        pygame.display.flip()