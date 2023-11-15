import pygame
import sys
sys.path.append('src')
from sample_controller import Controller
#import your controller

def main():
    pygame.init()
    screen = Controller()
    screen.mainloop()
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
