import pygame
class Constants:
    #file location of according images 
    MAPIMAGE = "assets/Map.png"
    MENUIMAGE = "assets/Menu.jpg"
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

    ENEMY_IMAGES = {
        "weak": "assets/Balloon/red_balloon.png",
        "medium": "assets/Balloon/green_balloon.png",
        "strong": "assets/Balloon/brown_balloon.png",
        "elite": "assets/Balloon/grey_balloon.png",
    }

    

    ENEMY_DATA = {
        "weak":{
            "health":10,
            "speed":2
        },
         "medium":{
            "health":15,
            "speed":4
        },
         "strong":{
            "health":20,
            "speed":6
        },
         "elite":{
            "health":30,
            "speed":10
        },
    }
   

