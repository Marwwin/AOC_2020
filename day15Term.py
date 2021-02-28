def playWordGame(inp,n):
    prev = 0

    for x in range(len(inp)+1,n):
        nxt = prev
        val = tuple(inp.keys())
        if val.count(nxt) == 1 :
            prev = x-inp[nxt]    
            inp.update({nxt:x})
        elif val.count(nxt) == 0:
            prev = 0
            inp.update({nxt:x})

    print(prev)

def makeMap(inp):
    theM = {}
    i = 1
    for x in inp:
        theM.update({x:i})
        i += 1
    return theM
    
import time

startTime = time.time()

inp = [19,20,14,0,9,1]
inp2 = [0,3,6]
newInp = makeMap(inp)

playWordGame(newInp,120000)
print("--- %s seconds ---" % (time.time() - startTime))
