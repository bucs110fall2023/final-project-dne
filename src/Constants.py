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
    ENEMY_IMAGES = {
      "weak": "assets/Balloon/red_balloon.png",
      "medium": "assets/Balloon/green_balloon.png",
      "strong": "assets/Balloon/brown_balloon.png",
      "elite": "assets/Balloon/grey_balloon.png",
    }
   #screen size for the gameplay area 
    TILESIZE = 16
    Rows = 45
    Cols = 62
    DEFAULT_X_GAME_SIZE = 992
    DEFAULT_Y_GAME_SIZE = 718 
    SPAWN_CD = 400