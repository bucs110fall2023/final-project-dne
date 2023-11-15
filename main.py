import pygame
from sample_controller import Controller
""" 
its not importing correctly for some reason 



"""
#import your controller

def main():
    pygame.init()
    screen = Controller()
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
