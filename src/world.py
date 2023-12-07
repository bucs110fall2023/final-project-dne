import pygame
import random
from src.Constants import Constants as C

class World():
    def __init__(self, MAPIMAGE, data=0):
        self.level = 1
        self.waypoints = []
        self.level_data = data 
        
        self.orignal_image = pygame.image.load(MAPIMAGE).convert_alpha()
        #code not used yet need to edit for better form 
        x,y =pygame.display.get_window_size()
        x = x*.72
        self.image = pygame.transform.scale(self.orignal_image, (x,y))
        self.x_factor = x/C.DEFAULT_X_GAME_SIZE
        self.y_factor = y/C.DEFAULT_Y_GAME_SIZE

        self.enemy_list = []
        self.spawned = 0
        
    def process_enemies(self):
        enemies = C.ENEMY_SPAWN_DATA[self.level-1]
        for enemy_type in enemies:
            enemies_to_spawn = enemies[enemy_type]
            for enemy in range(enemies_to_spawn):
                self.enemy_list.append(enemy_type)
        #randomize
        random.shuffle(self.enemy_list)
        
    #blits and redraws screen
    def draw(self,surface,cords=(0,0)):
        surface.blit(self.image,cords)
