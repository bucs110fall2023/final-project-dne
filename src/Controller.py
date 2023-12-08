import pygame
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
        self.last_spawn = pygame.time.get_ticks()
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

    #updates enemy data 
    self.enemy_group.update()

    #draws to screen
    self.enemy_group.draw(self.screen)
    self.monkey_group.draw(self.screen)

    #Checks spawn cooldown
    if pygame.time.get_ticks() - self.last_spawn > C.SPAWN_CD:
        #checks if all balloons in round have been spawned 
        if world.spawned < len(world.enemy_list):
            enemy_type = world.enemy_list[world.spawned]
            #spawns Enemy
            enemy = Enemy(enemy_type,((world.scale(C.WAYPOINTS))),C.ENEMY_IMAGES)
            self.enemy_group.add(enemy)
            #updates spawned count
            world.spawned += 1
            #resets cooldown
            self.last_spawn = pygame.time.get_ticks()

    #flips the screen         
    pygame.display.flip()

  
  def gameoverloop(self):
      #event loop
      pass
      #update data

      #redraw

