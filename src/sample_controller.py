import pygame
class Controller:
  
  def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024,1024))
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
    background_image = pygame.image.load("assets\Menu2.jpg")
    self.screen.blit(background_image, (0, 0))
    pygame.display.set_caption("menu")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            self.state = "game"
            self.screen.fill((0,0,0))
    pygame.display.flip()


  def gameloop(self):

     background_image = pygame.image.load("assets\class_diagram.jpg")
     self.screen.blit(background_image, (0, 0))   
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            print("gamestate")
     pygame.display.flip()
      #redraw
    
  def gameoverloop(self):
      #event loop
      pass
      #update data

      #redraw

