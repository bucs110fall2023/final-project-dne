import pygame
from src.world import World
from src.Constants import Constants as C
class Controller:
  
  def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        self.running = True
  def mainloop(self):
    self.state = "menu"
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
    world =World(C.MENUIMAGE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.state = "game"
                self.screen.fill((0,0,0))
    world.draw(self.screen)
        
            



  def gameloop(self):
     world = World(C.MAPIMAGE)
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

