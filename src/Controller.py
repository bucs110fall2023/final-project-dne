import pygame
import random as R
from src.world import World
from src.badguy import Enemy
from src.monkey import Monkey
from src.Constants import Constants as C
from src.Info import Info 
from pygame.math import Vector2
from pygame import mixer 

class Controller:
  def __init__(self):
        #inits pygame and sets screen size and start screen to the menu
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.running = True
        self.state = "menu"
        self.last_spawn = pygame.time.get_ticks()
        self.enemy_group = pygame.sprite.Group()
        self.monkey_group = pygame.sprite.Group()
        #pygame.mixer.init()
        #pygame.mixer.music.load('assets/music/music.wav')
        #pygame.mixer.music.set_volume(0.5)
        #pygame.mixer.music.play(-1)
        
  def mainloop(self):
    #swaps between differnt game stages 
    while self.running:
        if self.state == "menu":
            self.menuloop()
        elif self.state == "game":
            self.gameloop()
    else:
        pygame.quit()



    
  def menuloop(self):
    #loads the background image
    world = World(C.MENUIMAGE)  
    # proccesses events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        #if player hits space moves to next screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.state = "game"
                self.screen.fill((0,0,0))
    #blits and flips display
    world.draw(self.screen,(0,0))
    #button.draw(self.screen)
    pygame.display.flip()

  def gameloop(self):
    #loads map background
    self.screen.fill("brown")
    world = World(C.MAPIMAGE)
    world.draw(self.screen)

   
    
    #proccesses events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < C.DEFAULT_X_GAME_SIZE:
                monkey = Monkey(C.MONKEYIMAGE,mouse_pos)
                self.monkey_group.add(monkey) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_round = True
    
    #monkey attacks
    for monkey in self.monkey_group:
        monkey.attack(self.monkey_group,self.enemy_group,self.screen)
    
    #updates balloons
    self.enemy_group.update()

    #redraws enems
    self.enemy_group.draw(self.screen)
    self.monkey_group.draw(self.screen)
    
    #procceses order of enemies spwaning 
    world.process_enemies()

    #manages rate of spawning 
    if pygame.time.get_ticks() - self.last_spawn > C.SPAWN_CD:
        if world.spawned < len(world.enemy_list):
            enemy_type = world.enemy_list[world.spawned]
            enemy = Enemy(enemy_type,((world.scale(Info.waypoints_data))),C.ENEMY_IMAGES)
            self.enemy_group.add(enemy)
            world.spawned += 1
            self.last_spawn = pygame.time.get_ticks()


    #flips display
    pygame.display.flip()       