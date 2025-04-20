from ursina import *
from ursina.prefabs.first_person_controller import *
thegame = Ursina() #the game equals the ursina enviroment
window.title = "Strive" #set title
gametick = 0 # set game tick
window.borderless = False #set window bordered
window.fullscreen = False
cubes = [] #cube matrix
player = FirstPersonController(position=(0,26,0)) #set player to first person controller
player.gravity = 1 #set gravity to 0
for i in range(16):
    for j in range(16):
        for k in range(16):
            cubes.append(Entity(model='cube', color=color.rgb((i*16)-1,(j*16)-1,(k*16)-1), position=(i+(16*chunks),j+(16*chunks),k+(16*chunks)), texture='white_cube', collider='box', scale=(1,1,1))) # create a cube matrixd
def input(key): #input function
    if key == 'right mouse down' and mouse.hovered_entity:
        cubes.append(Entity(model='cube', color=mouse.hovered_entity.color, position=(mouse.hovered_entity.x+mouse.normal[0],mouse.hovered_entity.y+mouse.normal[1],mouse.hovered_entity.z+mouse.normal[2]), texture='white_cube', collider='box', scale=(1,1,1),))
    if key == 'left mouse down' and mouse.hovered_entity:
        mouse.hovered_entity.disable() #die
def update():
    global gametick # make gametick global
    global cubes # make cubes global
    gametick +=1 #increment game tick
thegame.run() # run the game