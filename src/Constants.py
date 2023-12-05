import pygame
class Constants:
    #file location of according images 
    MAPIMAGE = "assets/Map.png"
    MENUIMAGE = "assets/Menu.jpg"
    ENEMYIMAGE = "assets/Balloon.png"
    MONKEYIMAGE =  "assets/Monkey.jpg"
    BUTTONIMAGE = "assets/Basic_red_dot.png"
   

   #screen size for the gameplay area 
    
    TILESIZE = 32
    Rows = 48
    Cols = 30
    DEFAULTSCREENWIDTH= TILESIZE * Rows
    DEFAULTSCREENHEIGHT = TILESIZE * Cols
  
    

    #Leaves room for side bar
    MENUSIZE = 200

    #the path the enemies will travel
    WAYPOINTS = [
        (100,100),
        (400,200),
        (400,100),
        (200,300)
    ]