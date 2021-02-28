#%%

def getNewPos(boatPos, direction, vel):
    vel = int(vel)
    if direction == "N":
        boatPos[0] += vel
    elif direction == "S":
        boatPos[0] -= vel
    elif direction == "E":
        boatPos[1] += vel
    elif direction == "W":
        boatPos[1] -= vel
    return boatPos

def getVaderStrack(d):
    if d == 90:
        return "E"
    elif d == 180:
        return "S"
    elif d == 270:
        return "W"
    elif d == 0:
        return "N"

lines = open("day12.txt","r").readlines()

lines = [[l[0],int(l[1:])] for l in lines]

boat = [0,0]
boatDir = 90

for l in lines:
    if l[0] == "F":
        boat = getNewPos(boat,getVaderStrack(boatDir),l[1])
    elif l[0] == "R":
        boatDir += l[1]
        boatDir = boatDir%360
    elif l[0] == "L":
        boatDir -= l[1]
        boatDir = boatDir%360
    else:
        boat = getNewPos(boat,l[0],l[1])
print(abs(boat[0])+abs(boat[1]))
# %%
