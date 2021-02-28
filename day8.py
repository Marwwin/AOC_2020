#%%
lines = []
with open("day8.txt","r") as a:
    lines = a.readlines()

accumulator = 0
index = 0
hist = []
splitted = [l.split(" ") for l in lines]

while True:
    hist.append(index)
    if splitted[index][0] == "acc":
        accumulator = accumulator + int(splitted[index][1].strip())
        index = index + 1
    elif splitted[index][0] == "jmp":
        index = index + int(splitted[index][1])
    elif splitted[index][0] == "nop":
        index = index + 1
    if index in hist:
        print(accumulator)
        print(hist.index(108))
        print(splitted[463])
    
        break

#%%
lines = []
with open("day8.txt","r") as a:
    lines = a.readlines()

def chang(lst,strg, n):
    hit = 0
    for l in lst:
        if l[0] == "nop":
            hit = hit +1
        if hit == n:
            print("found Hit")
            l[0] = strg;
            return lst

def testL(lst):
    accumulator = 0
    index = 0
    hist = []
    splitted = lst
    while True:
        hist.append(index)
        #print(index)
        #print(splitted[index], index)
        if splitted[index][0] == "acc":
            accumulator = accumulator + int(splitted[index][1].strip())
            index = index + 1
        elif splitted[index][0] == "jmp":
            index = index + int(splitted[index][1])
        elif splitted[index][0] == "nop":
            index = index + 1
        if index > len(splitted):
            print(accumulator)
            print("end ",index)
            return True
        if index in hist:
            #print(accumulator)
            print("Loop",accumulator)
            return False


theL = [l.split(" ") for l in lines]
i = 1
while True:
    cpL = theL.copy()
    #print(cpL)
    lst = chang(cpL, "jmp",i)
    
    isT = testL(lst)
    if isT:
        break
    i = i+1

#%%
instructions = []
with open('day8.txt') as fp:
    line = fp.readline()
    while line:
        tokens = line.strip().split()
        instructions.append((tokens[0], int(tokens[1])))
        line = fp.readline()

def execute(instrs):
    hasLoop = False
    visited = set()
    ptr = acc = 0
    while ptr < len(instrs):
        op, value = instrs[ptr]
        if ptr in visited:
            hasLoop = True
            break
        visited.add(ptr)
        if op == 'jmp':
            ptr = ptr + value
            continue
        elif op == 'acc':
            acc = acc + value
        ptr = ptr + 1
    return (acc, hasLoop)

print(f'Part 1\n{execute(instructions)[0]}\n')

swapDict = {'nop':'jmp','jmp':'nop'}
for i, (op,value) in enumerate(instructions):
    if op == 'nop' or op == 'jmp':
        swappedOp = [(swapDict[op], value)]
        newInstructions = instructions[:i] + swappedOp + instructions[i+1:]
        accValue, hasLoop = execute(newInstructions)
        if not hasLoop:
            print(f'Part 2\n{accValue}')