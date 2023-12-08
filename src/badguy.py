import pygame
from src.Constants import Constants as C
from pygame.math import Vector2
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self,type,waypoints,images):
        super().__init__()
        #set up enemy intial conditions 
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = C.ENEMY_DATA.get(type)["health"]
        self.speed =  C.ENEMY_DATA.get(type)["speed"]
        self.angle = 0
        #loads and scales image based off screen size
        self.orignal_image = pygame.image.load(images.get(type)).convert_alpha()
        self.scaled_image =  pygame.transform.scale(self.orignal_image, (30,30))
        self.image = pygame.transform.rotate(self.scaled_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def update(self):
        self.move()
        self.rotate()
    
    def move(self):
        #set target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            #has reached end of track
            self.kill()

        #calculate distance to target 
        distance = self.movement.length()
        #check remaining distance speed 
        if distance >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            #prevents overshooting waypoint
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            self.target_waypoint += 1
   
   
    def rotate(self):
        
        #calc distance to next point 
        dist = self.target - self.pos
        #calculate angle of rotation 
        self.angle = math.degrees(math.atan2(-dist[1],dist[0])) % 180
        self.image = pygame.transform.rotate(self.scaled_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
       