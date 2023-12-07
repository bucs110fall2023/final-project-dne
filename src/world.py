import pygame
import random
from src.Constants import Constants as C

class World():
    def __init__(self, MAPIMAGE, data=0):
        self.level = 1
        self.waypoints = []
        self.level_data = data 
        self.image = pygame.image.load(MAPIMAGE).convert_alpha()
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
    def draw(self,surface,cords=(-255,-315)):
        surface.blit(self.image,cords)
