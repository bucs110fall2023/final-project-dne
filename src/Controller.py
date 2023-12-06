import pygame
import json
import random as R
from src.world import World
from src.badguy import Enemy
from src.monkey import Monkey
from src.Constants import Constants as C
from src.button import Button




class Controller:
  
  def __init__(self):
        #inits pygame and sets screen size and start screen to the menu
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.running = True
        self.state = "menu"
        self.enemy_group = pygame.sprite.Group()
        self.monkey_group = pygame.sprite.Group()
        
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
    world =World(C.MENUIMAGE)
    #button = Button(C.XWINDOWSIZE +10, C.YWINDOWSIZE -20, C.BUTTONIMAGE)
    
    
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
    world.draw(self.screen)
    #button.draw(self.screen)
    pygame.display.flip()
        
            


  def gameloop(self):
    #loads map background
    self.screen.fill("brown")
    world = World(C.MAPIMAGE)
    world.draw(self.screen)
    pygame.draw.lines(self.screen,"grey0",False,C.WAYPOINTS)
    #proccesses events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < C.DEFAULTSCREENWIDTH and mouse_pos[1] < C.DEFAULTSCREENHEIGHT:
                monkey= Monkey(C.MONKEYIMAGE,mouse_pos)
                self.monkey_group.add(monkey)
        if event.type == pygame.KEYDOWN:
            enemy = Enemy(C.WAYPOINTS,C.ENEMYIMAGE)
            self.enemy_group.add(enemy)
    self.enemy_group.update()
    self.enemy_group.draw(self.screen)
    self.monkey_group.draw(self.screen)
    pygame.display.flip()
  
  
  
  def gameoverloop(self):
      #event loop
      pass
      #update data

      #redraw

