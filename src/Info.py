import json 

class Info:
    #opens file 
    with open("src/DATA/game_data.json", "r") as json_file:
        game_data = json.load(json_file)
    #seperates data classes
    enemy_data = game_data["enemy_data"]
    enemy_spawn_data = game_data["enemy_spawn_data"]
    waypoints_data = game_data["waypoints"]