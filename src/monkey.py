import pygame
from src.Constants import Constants as C

class Tower(pygame.sprite.Sprite):
    def __init__(self,image,pos,):
        pygame.sprite.Sprite.__init__(self)
        #corrects to center over tile
        self.tile_x = pos[0] // C.TILESIZE
        self.tile_y = pos[1] // C.TILESIZE
        self.x = (self.tile_x +.5) * C.TILESIZE
        self.y = (self.tile_y +.5) * C.TILESIZE

        self.range = 90
        self.selected = False
        
        #loads and scales image 
        self.image = pygame.image.load(image)
        self.image= pygame.transform.scale(self.image,(C.TILESIZE,C.TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.center = ((self.x,self.y))

    #create transparent showing range circle 
        self.range_image = pygame.Surface((self.range*2,self.range*2))
        self.range_image.fill((1,1,1))
        self.range_image.set_colorkey((1,1,1))
        pygame.draw.circle(self.range_image,"grey100",(self.range,self.range),self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self,surface):
        surface.blit(self.image,self.rect)
        if self.selected:
            surface.blit(self.range_image,self.range_rect)

    def selected_Tower(mouse_pos,group):
        tile_x = mouse_pos[0] // C.TILESIZE
        tile_y = mouse_pos[1] // C.TILESIZE
        x = (tile_x +.5) * C.TILESIZE
        y = (tile_y +.5) * C.TILESIZE
        for Tower in group:
            if (x,y)== (Tower.tile_x,Tower.tile_y):
                return Tower
    
    def attack(self, balloons):
        for balloon in balloons:
            distance = ((self.x - balloon.x)**2 + (self.y - balloon.y)**2)**0.5
            if distance <= self.range:
                balloons.remove(balloon)

    

    