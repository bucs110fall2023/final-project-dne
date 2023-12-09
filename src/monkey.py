import pygame
from src.Constants import Constants as C
import math 
from src.world import World

class Monkey(pygame.sprite.Sprite):
    def __init__(self,image,pos,):
        pygame.sprite.Sprite.__init__(self)
        #corrects to center over tile
        self.tile_x = pos[0] // C.TILESIZE
        self.tile_y = pos[1] // C.TILESIZE
        self.x = ((self.tile_x +.5) * C.TILESIZE)
        self.y = ((self.tile_y +.5) * C.TILESIZE)

        #sets attack variables 
        self.range = 500
        self.last_attack = pygame.time.get_ticks()
        self.cd = 1000
        
        #loads and scales image 
        self.image = pygame.image.load(image)
        self.image= pygame.transform.scale(self.image,(C.TILESIZE*3,C.TILESIZE*3))
        self.rect = self.image.get_rect()
        self.rect.center = ((self.x,self.y))

    #draws monkey 
    def draw(self,surface):
        surface.blit(self.image,self.rect)

    
    def attack(self, monkey_group, enemy_list, screen):
        for monkey in monkey_group:
            if pygame.time.get_ticks() - monkey.last_attack > monkey.cd and len(enemy_list) != 0:
                closest_enemy = None
                min_distance = monkey.range + 1  # Set initial min_distance to a value greater than monkey.range

                for enemy in enemy_list:
                    distance = math.hypot(self.rect.centerx - enemy.rect.center[0], self.rect.centery - enemy.rect.center[1])

                    if distance < monkey.range and distance < min_distance:
                        closest_enemy = enemy
                        min_distance = distance

                if closest_enemy is not None:
                    pygame.draw.line(screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), (closest_enemy.rect.center[0], closest_enemy.rect.center[1]))
                    #enemy_list.remove(closest_enemy)
                    closest_enemy.health = closest_enemy.health -5
                    monkey.last_attack = pygame.time.get_ticks()
    

    