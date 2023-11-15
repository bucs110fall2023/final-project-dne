import pygame
class Controller:
  
  def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
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
    else:
        pygame.quit()


    ### below are some sample loop states ###

  def menuloop(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            self.state = "game"


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

