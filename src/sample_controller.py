import pygame
class Controller:
  
  def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defense")
        self.running = True
  def mainloop(self):
    #select state loop
    self.state = "menu"
    while self.running:
        if self.state == "menu":
            self.menuloop()
        elif self.state == "game":
            self.gameloop()
        elif self.state == "gameover":
            self.gameoverloop()
    ### below are some sample loop states ###

  def menuloop(self):
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.K_KP_ENTER:
              self.state= "game"
      bg = pygame.image.load("assets\gui.jpg")
      self.screen.blit(bg, (0, 0))
      
  def gameloop(self):
      #event loop
      #update data
      pass
      #redraw
    
  def gameoverloop(self):
      #event loop
      pass
      #update data

      #redraw

