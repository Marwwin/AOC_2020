#%%

def getPrevious(li,x):
    for i in reversed(range(len(li)-1)):
        if li[i] == x:
            return i    

inp = [19,20,14,0,9,1]
counter = 0
testi = [19,20,14,0,9,1]

for x in testi:
    if counter >= len(testi)-1:
        if testi.count(x) == 1:
            testi.append(0)
        elif testi.count(x) > 1:
            last = getPrevious(testi,x)
            testi.append(counter - last)
    if counter == 30000000-1:
        30000000
        print(x)
        break
    counter += 1


#%%

def playWordGame(inp,n):
    prev = 0

    for x in range(len(inp)+1,n):
        nxt = prev
        val = tuple(inp.keys())
        if nxt in val :
            prev = x-inp[nxt]    
            inp.update({nxt:x})
        else:
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
newInp = makeMap(inp)

playWordGame(newInp,300000)
print("Python 300000 numbers counted")
print("--- %s seconds ---" % (time.time() - startTime))
