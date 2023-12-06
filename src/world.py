import pygame
from src.Constants import Constants as C
class World():
    def __init__(self, MAPIMAGE, data=0):
        self.waypoints = []
        self.level_data = data 
        self.image = pygame.image.load(MAPIMAGE)

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
    
    #blits and redraws screen
    def draw(self,surface,cords=(0,0)):
        surface.blit(self.image,cords)