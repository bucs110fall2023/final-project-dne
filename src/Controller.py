import pygame
import random as R
from src.world import World
from src.badguy import Enemy
from src.monkey import Monkey
from src.Constants import Constants as C
from src.button import Button
from src.Info import Info 
from pygame.math import Vector2


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
        self.button_group=[]
        self.gamehealth = 1
        
  def mainloop(self):
    #swaps between differnt game stages 
    while self.running:
        if self.state == "menu":
            self.menuloop()
        elif self.state == "game":
            self.gameloop()
        elif self.state == "gameover":
            self.gameoverloop()
    else:
        pygame.quit()


    ### below are some sample loop states ###
    
  def menuloop(self):
    #loads the background image
    world = World(C.MENUIMAGE)
  #def button(self):
    #placing = False 
    #button = Button((500,500), C.BUYIMAGE, True)
    #cancel_button = Button((400,400), C.CANCELIMAGE, True)
    #if button.draw(self.screen):
        #placing = True 
    #if placing == True:
        #if cancel_button.draw(self.screen):
            #placing = False 
        
    
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
    world.process_enemies()
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
                #monkeybutton = Button(1200,100, C.MONKEYIMAGE, True)
                #self.button_group.append(monkeybutton)
                
            
                
        if event.type == pygame.KEYDOWN:
           """
            enemy_type = "elite"
            enemy = Enemy(enemy_type,C.waypoints_data,C.ENEMY_IMAGES)
            self.enemy_group.add(enemy)
           """
    for monkey in self.monkey_group:
        monkey.attack(self.monkey_group,self.enemy_group,self.screen)


    self.enemy_group.update()
    self.enemy_group.draw(self.screen)
    self.monkey_group.draw(self.screen)
    for i in self.button_group:
        i.draw(self.screen)
    



    if pygame.time.get_ticks() - self.last_spawn > C.SPAWN_CD:
        if world.spawned < len(world.enemy_list):
            enemy_type = world.enemy_list[world.spawned]
            enemy = Enemy(enemy_type,((world.scale(Info.waypoints_data))),C.ENEMY_IMAGES)
            self.enemy_group.add(enemy)
            world.spawned += 1
            self.last_spawn = pygame.time.get_ticks()
    
    if self.gamehealth == 0:
        self.state="gameover"

    def buttons():
        MONKEYBUTTON = Button(C.DEFAULT_X_GAME_SIZE + 50,50, C.MONKEYIMAGE, True)
        CANCELBUTTON = Button(C.DEFAULT_X_GAME_SIZE + 50, 100, C.CANCELIMAGE, True)
        UPGRADEBUTTON = Button(C.DEFAULT_X_GAME_SIZE + 50, 150, C.UPGRADEIMAGE, True)
        PLAYBUTTON = Button(C.DEFAULT_X_GAME_SIZE + 50, 200, C.PLAYIMAGE, True)
        REPLAYBUTTON = Button(50, 250, C.REPLAYIMAGE, True)
        FASTBUTTON = Button(C.DEFAULT_X_GAME_SIZE + 50, 300, C.FASTIMAGE, False)
        MONKEYBUTTON.draw(self.screen)
        CANCELBUTTON.draw(self.screen)
        UPGRADEBUTTON.draw(self.screen)
        PLAYBUTTON.draw(self.screen)
        REPLAYBUTTON.draw(self.screen)
        FASTBUTTON.draw(self.screen)

    pygame.display.flip()       





  
  def gameoverloop(self):
      #event loop
    pass
      #update data
    self.screen.fill((0,0,0))
      #redraw

