# %%

def test25(n, lin):
    isT = False
    for i in range(0, 25):
        for j in range(i, 25):
            if lin[i]+lin[j] == n:
                isT = True
    return isT


lines = []
with open("day9.txt","r") as a:
    lines = a.readlines()

lines = [int(l.strip()) for l in lines]

#print(lines[0:25])
for i in range(25, len(lines)):
    isT = test25(lines[i], lines[i-25:i])
    if isT == False:
        print(lines[i], i)

        # print(i)

#%%

def testN(n,lin):
    res = 0
    lis = []
    i = 0
    while True:
        if sum(lis) == n:
            print(min(lis)+max(lis))
            return True 
        elif sum(lis) > n:
            res = 0
            lis = []
            return False
        else:
            lis.append(lin[i])
            i = i+1

lines = []
with open("day9.txt","r") as a:
    lines = a.readlines()

lines = [int(l.strip()) for l in lines]
lis = []
for i in range(0,len(lines)):
    isT = testN(1639024365,lines[i:len(lines)])
    if isT == True:
        print("Found")
        break


