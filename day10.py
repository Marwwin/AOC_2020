
#%%

def testOne(jolts,current):
    for j in jolts:
        if j == current+1:
            return True
    return False
def testThree(jolts,current):
    for j in jolts:
        if j == current+3:
            return True
    return False

lines = []
with open("day10.txt","r") as a:
    lines = a.readlines()

jolts = [int(l.strip()) for l in lines]
current = 0
oneJ = 0
threeJ = 0
while True:
    print("start",current,oneJ,threeJ)
    one = testOne(jolts,current)
    three = False
    if one:
        current = current +1
        oneJ = oneJ +1
    else:
        three = testThree(jolts,current)
        threeJ = threeJ + 1
    if three:
        current = current + 3
    if one == False and three == False:
        print("Not Found",one)
        print(oneJ * threeJ)
        break

#%%
def testOne(jolts,current):
    for j in jolts:
        if j == current+1:
            return True
    return False
def testTwo(jolts,current):
    for j in jolts:
        if j == current+2:
            return True
    return False
def testThree(jolts,current):
    for j in jolts:
        if j == current+3:
            return True
    return False

test = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

one = 0
two = 0
three = 0
for t in test:
    on = testOne(test,t)
    tw = testTwo(test,t)
    th = testThree(test,t)
    if on:
        one = one + 1
    if tw:
        two = two + 1
    if th:
        three = three + 1

print(one*two*three)
print(one+two+three)

1,1,3,2,1,2,1,1

