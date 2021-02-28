#%%

def playGame(p1, p2):
    p1h = p1[0]
    p2h = p2[0]
    newp1 = []
    newp2 = []
    if p1h < p2h:
        newp1 = p1[1:]
        newp2 = p2[1:] + [p2h] + [p1h]
    else:
        newp2 = p2[1:]
        newp1 = p1[1:] + [p1h] + [p2h]
    return newp1,newp2

def showResult(player):
    i = 1
    sum = 0
    player1.reverse()
    for p in player1:
        sum +=  (i * p)
        i += 1
    print(sum)

lines = open("day22.txt").readlines()

player1 = [int(l.strip()) for l in lines[1:26]]
player2 = [int(l.strip()) for l in lines[28:]]

while True:
    if len(player1) == 0 or len(player2) == 0:
        break
    player1, player2 = playGame(player1,player2)

showResult(player1 if len(player2) == 0 else player2)
#%%
# PART 2

def recursiveCombat(p1,p2):
    pair = (p1,p2)
    if pair in memory:

def playGame(p1, p2):
    p1h = p1[0]
    p2h = p2[0]
    newp1 = []
    newp2 = []
    if p1h < p2h:
        newp1 = p1[1:]
        newp2 = p2[1:] + [p2h] + [p1h]
    else:
        newp2 = p2[1:]
        newp1 = p1[1:] + [p1h] + [p2h]
    return newp1,newp2

def showResult(player):
    i = 1
    sum = 0
    player1.reverse()
    for p in player1:
        sum +=  (i * p)
        i += 1
    print(sum)

lines = open("day22.txt").readlines()

player1 = [int(l.strip()) for l in lines[1:26]]
player2 = [int(l.strip()) for l in lines[28:]]

memory = []
while True:
    if len(player1) == 0 or len(player2) == 0:
        break
    player1, player2 = playGame(player1,player2)

winner = recursiveCombat(player1,player2)

showResult(winner)