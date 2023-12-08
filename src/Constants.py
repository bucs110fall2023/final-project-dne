import pygame
class Constants:
    #file location of according images 
    MAPIMAGE = "assets/Mapnew.png"
    MENUIMAGE = "assets/Menu.jpg"
    MONKEYIMAGE =  "assets/Monkey.jpg"
    BUYIMAGE = "assets/Buy.png"
    CANCELIMAGE = "assets/Cancel.png"
    BACKGROUNDIMAGE = "assets/background.jpg"
    REPLAYIMAGE = "assets/Replay.png"
    PLAYIMAGE = "assets/Play.png"
    FASTIMAGE = "asset/Fast Foward.png" 
    UPGRADEIMAGE = "asset/Upgrade.png"
    COINIMAGE = "asset/Coin.jpg"
   #screen size for the gameplay area 
    TILESIZE = 32
    Rows = 30
    Cols = 31
    DEFAULT_X_GAME_SIZE = 992
    DEFAULT_Y_GAME_SIZE = 718 
  

    #the path the enemies will travel
    SPAWN_CD = 400
    WAYPOINTS = [
        (46,0),
        (46,275),
        (248,275),
        (248,189),
        (421,189),
        (421,419),
        (190,419),
        (190,505),
        (550,505),
        (550,101),
        (435,101),
        (435,15),
        (695,15),
        (695,520),
        (780,520),
        (780,417),
        (880,417),
        (880,75)
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

    ENEMY_SPAWN_DATA = [
  {
    #1
    "weak": 1,
    "medium": 2,
    "strong": 3,
    "elite": 4
  },
  {
    #2
    "weak": 30,
    "medium": 0,
    "strong": 0,
    "elite": 0
  },
  {
    #3
    "weak": 20,
    "medium": 5,
    "strong": 0,
    "elite": 0
  },
  {
    #4
    "weak": 30,
    "medium": 15,
    "strong": 0,
    "elite": 0
  },
  {
    #5
    "weak": 5,
    "medium": 20,
    "strong": 0,
    "elite": 0
  },
  {
    #6
    "weak": 15,
    "medium": 15,
    "strong": 4,
    "elite": 0
  },
  {
    #7
    "weak": 20,
    "medium": 25,
    "strong": 5,
    "elite": 0
  },
  {
    #8
    "weak": 10,
    "medium": 20,
    "strong": 15,
    "elite": 0
  },
  {
    #9
    "weak": 15,
    "medium": 10,
    "strong": 5,
    "elite": 0
  },
  {
    #10
    "weak": 0,
    "medium": 100,
    "strong": 0,
    "elite": 0
  },
  {
    #11
    "weak": 5,
    "medium": 10,
    "strong": 12,
    "elite": 2
  },
  {
    #12
    "weak": 0,
    "medium": 15,
    "strong": 10,
    "elite": 5
  },
  {
    #13
    "weak": 20,
    "medium": 0,
    "strong": 25,
    "elite": 10
  },
  {
    #14
    "weak": 15,
    "medium": 15,
    "strong": 15,
    "elite": 15
  },
  {
    #15
    "weak": 25,
    "medium": 25,
    "strong": 25,
    "elite": 25
  }
]


   

