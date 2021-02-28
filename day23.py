
#%%

def getDestination(inp,curr):
    offset = 1
    while True:
        if curr-offset < min(inp):
            return max(inp)
        elif curr-offset in inp:
            return (curr-offset) 
        offset += 1


def crabCups(inp):
    curr = inp[0]
    pickup = inp[1:4]
    other = inp[4:]
    destination = getDestination(other,curr)
    destinationIndex = other.index(destination)
    return other[0:destinationIndex+1] + pickup + other[destinationIndex+1:] + [curr]

inp = [3,8,9,1,2,5,4,6,7]
inp2 = [2,8,4,5,7,3,9,6,1]
for i in range(100):
    inp2 = crabCups(inp2)

print(inp2)