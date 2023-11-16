import pygame
from src.world import World
from src.Constants import Constants as C
class Controller:
  
  def __init__(self):
        #inits pygame and sets screen size and start screen to the menu
        pygame.init()
        self.screen = pygame.display.set_mode((900,700))
        self.running = True
        self.state = "menu"
  
  
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
        
            



  def gameloop(self):
     #loads map background
     world = World(C.MAPIMAGE)
     #proccesses events
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            print("gamestate")
     world.draw(self.screen)
      #redraw
    
  def gameoverloop(self):
      #event loop
      pass
      #update data

      #redraw

