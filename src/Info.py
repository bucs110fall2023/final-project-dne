import json 

class Info:
    with open("src/DATA/game_data.json", "r") as json_file:
        game_data = json.load(json_file)

    enemy_data = game_data["enemy_data"]
    enemy_spawn_data = game_data["enemy_spawn_data"]
    waypoints_data = game_data["waypoints"]