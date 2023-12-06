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
    """

    #extract data 
    def process_data(self):
        if self.level_data != 0:
            for layer in self.level_data["layers"]:
                if layer["name"] == "waypoints":
                    for obj in layer ["objects"]:
                        waypoint_data = obj["polyline"]
                        self.process_waypoints(waypoint_data)

    def process_waypoints(self, data):
        for point in data:
            temp_x = point.get("x")
            temp_y = point.get("y")
            self.waypoints.append((temp_x, temp_y))     
            """
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