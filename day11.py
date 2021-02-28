#%%
# PART 1
flatten = lambda x: [item for sublist in x for item in sublist]

def analyzeSurrounding(inp,current):
    dlist = flatten(inp)
    res = False
    if current  == "L":
        res = all(x =="L" or x == "." for x in dlist)
    elif current == "#":
        res = True if "".join(dlist).count("#") >= 4 else False 
    return res

def getSurrounding(inp,row,seat):
    ls = [ inp[row-1][seat-1] if row != 0 and seat != 0 else []\
                    ,inp[row-1][seat] if row != 0  else []\
                    ,inp[row-1][seat+1] if row != 0 and seat != len(inp[0])-1  else [] \
                    ,inp[row][seat-1] if seat != 0  else []\
                    ,inp[row][seat+1] if seat != len(inp[0])-1 else []   \
                    ,inp[row+1][seat-1] if row < len(inp)-1 and seat != 0  else [] \
                    ,inp[row+1][seat] if row < len(inp)-1 else [] \
                    ,inp[row+1][seat+1] if row < len(inp)-1 and seat < len(inp[0])-1  else []]
    return ls

def newRound(inp):
    result = []
    rowCounter = 0
    for row in range(0,len(inp)):
        newRow = ""
        for seat in range(0,len(inp[0])):
            curr = inp[row][seat]
            flipSeat = False
            res = ""
            if curr != ".":
                    ls = getSurrounding(inp,row,seat)
                    flipSeat = analyzeSurrounding(ls,curr)
            if flipSeat:
                if curr == "L":
                    res = "#"
                elif curr == "#":
                    res = "L"
            else:
                res = curr
            newRow += res
        result.append(newRow)
    return result

lines = []
with open("day11.txt","r") as a:
    lines  = a.readlines()

dmap = [l.split("\n")[0] for l in lines]
mapCopy = dmap.copy()
while True:
    newMap = newRound(mapCopy)
    if newMap == mapCopy:
        #print(newMap)
        print("".join(newMap).count("#"))
        break
    else:
        mapCopy = newMap.copy()


#%%
# PART 2
flatten = lambda x: [item for sublist in x for item in sublist]

def analyzeSurrounding(inp,current):
    dlist = flatten(inp)
    res = False
    if current  == "L":
        res = all(x =="L" or x == "." for x in dlist)
    elif current == "#":
        res = True if "".join(dlist).count("#") >= 5 else False 
    return res
    

def getNextSeat(inp,row,rowDirection,seat,seatDirection):
    if row+rowDirection < 0 or row+rowDirection >= len(inp):
        return "."
    elif seat+seatDirection < 0 or seat+seatDirection >=len(inp[0]):
        return "."
    else:
        curr = inp[row+rowDirection][seat+seatDirection]
        if curr == "L" or curr == "#":
            return curr
        else:
            res = getNextSeat(inp,row+rowDirection,rowDirection,seat+seatDirection,seatDirection)
            #print(res)

            return res

def getSurrounding(inp,row,seat):
    ls = [ getNextSeat(inp,row,-1,seat,-1) if row != 0 and seat != 0 else [] \
                    ,getNextSeat(inp,row,-1,seat,0) if row != 0  else [] \
                    ,getNextSeat( inp,row,-1,seat,1) if row != 0 and seat != len(inp[0])-1  else [] \
                    ,getNextSeat(inp,row,0,seat,-1) if seat != 0  else [] \
                    ,getNextSeat(inp,row,0,seat,1) if seat != len(inp[0])-1 else [] \
                    ,getNextSeat(inp,row,1,seat,-1) if row < len(inp)-1 and seat != 0  else [] \
                    ,getNextSeat(inp,row,1,seat,0) if row < len(inp)-1 else [] \
                    ,getNextSeat(inp,row,1,seat,1) if row < len(inp)-1 and seat < len(inp[0])-1  else []]
    return ls

def newRound(inp):
    result = []
    rowCounter = 0
    for row in range(0,len(inp)):
        newRow = ""
        for seat in range(0,len(inp[0])):
            curr = inp[row][seat]
            flipSeat = False
            res = ""
            if curr != ".":
                    ls = getSurrounding(inp,row,seat)
                    flipSeat = analyzeSurrounding(ls,curr)
            if flipSeat:
                if curr == "L":
                    res = "#"
                elif curr == "#":
                    res = "L"
            else:
                res = curr
            newRow += res
        result.append(newRow)
    return result

lines = []
with open("day11.txt","r") as a:
    lines  = a.readlines()

dmap = [l.split("\n")[0] for l in lines]
mapCopy = dmap.copy()
while True:
    newMap = newRound(mapCopy)
    if newMap == mapCopy:
        #print(newMap)
        print("".join(newMap).count("#"))
        break
    else:
        mapCopy = newMap.copy()

# %%
