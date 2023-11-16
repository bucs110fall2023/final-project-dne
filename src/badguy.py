import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self,cords,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = cords
    
    def update(self):
        self.move()
    
    def move(self):
        self.rect.x += 10