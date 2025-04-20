from ursina import *

thegame = Ursina() #the game equals the ursina enviroment
window.title = "Strive" #set title
gametick = 0 # set game tick
controltick = 0 # set control tick
chunks = 0
window.borderless = False #set window bordered
window.fullscreen = False
cubes = [] #cube matrix
def update():
    global gametick # make gametick global
    global controltick # make controltick global
    global cubes # make cubes global
    global chunks # make chunks global
    gametick +=1 #increment game tick
    controltick -=1 #decrement control tick
    if held_keys['g'] and controltick <= 0: # if g is pressed and controltick is less than or equal to 0 then continue the program
        for i in range(16): # loop through the range of 5
            cubes.append([]) # append an empty list to cubes
            for j in range(16): # loop through the range of 5
                cubes[len(cubes)-1].append(Entity(model='cube', color=color.red, position=(i,j,0), scale=(1,1,1))) # append a cube to the last list in cubes
                j+=1
            i+=1
        print(gametick)
        print("gg") #show that the if statement was executed
        controltick = 16 # reset controltick to 4 so that we have ti wait another 4 ticks to press g again
        chunks += 1
        print (chunks)
thegame.run() # run the game