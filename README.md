[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803323&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# baboons vs balloons 
## CS110 Final Project fall, 2023 

## Team Members


*** Jay Shi, Scott Mcstay 

## Project Description

A tower defense game where balloons follow a set path and the the baboons need to attack and stop them from making it to the exit 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/Map.png)

## Program Design

### Features

1. Menu where user can ready up and start the game  
2. ability to place down attacking troops and not allowing them to stack 
3. the abilty to upgrade and deal more damage/range/attack speed
4. a wave system that can auto spawn in enemy charhcters 
5. differnt balloon types 
6. balloons follow a set track 
7. health is automatically reduced once balloons reach the end of the track
8. If Health hits 0 gameover is started
9. if all rounds are beaten victory screen  


### Classes

- Enemy Class 
    -creates and manages movement for the enemy ballon types
- Monkey Class
    - handles the spawning and targerting of all towers the user places while preventing overlapping of towers
- World Class 
    -loads, scales, and draws the background of the maps while also randomizing the order in which balloons appear in each round
- Button Class
    - Create various buttons that once clicked allow users to place/upgrade towers
- Constants Class
    - stores the data for variables that remain constant 

## ATP

|Step| Action  | Result |
|-|-----------------| --------------                             |
|1| Press Space key | updates from menu screen into game screen  |
|2| click on the Buy Button | toggles the buy button and allows user to click again to place the turret|
|3| click on the screen near the track| places a turret|
|4| Press start round button| starts spawning balloons on the track|
|5| more info | more info |
