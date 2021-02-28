#%%
import re

def runMask(mask,value):

    binaryValue = format(int(value), "036b")
    newValue = ""
    mask = mask[7:]
    for v in range(len(mask)):
        if mask[v] == "X":
            newValue += binaryValue[v]
        else:
            newValue += mask[v]
    return newValue

def runMemory(data,memory):
    mask = data[0]
    values = data[1:]
    for v in values:
        digits = re.findall("\d{1,}",v)
        memoryLoc = digits[0]
        maskedValue = runMask(mask,digits[1])
        memory.update({memoryLoc:maskedValue})
    return memory


lines = []
with open("day14.txt","r")as a:
    lines = a.readlines()

memory = {}
data = []
oneMask = []

for l in range(len(lines)):
    if l == 0:     
        oneMask.append(lines[l])
    elif l == len(lines)-1:
        oneMask.append(lines[l])
        data.append(oneMask)
    elif "mask" in lines[l]:
        data.append(oneMask)
        oneMask = []
        oneMask.append(lines[l])
    else:
        oneMask.append(lines[l])

print(data)

res = {}
for d in data:
    r = runMemory(d,memory)
    res.update(r)

sum = 0
for r in res:
    sum += int(res[r],2)
print(sum)


#%%
#PART 2

import re

def runMask(mask,value):

    binaryValue = format(int(value), "036b")
    newValue = ""
    mask = mask[7:]
    for v in range(len(mask)):
        if mask[v] == "X":
            newValue += "X"
        elif mask[v] == "1":
            new = binaryValue[v]
            if new == "0":
                newValue += "1"
            else:
                newValue += "0"
            
        else:
            newValue += mask[v]
    return newValue

def runMemory(data,memory):
    mask = data[0]
    values = data[1:]
    print("data",data)
    for v in values:
        print(v)
        digits = re.findall("\d{1,}",v)
        memoryLoc = digits[0]
        maskedValue = runMask(mask,digits[1])
        memory.update({memoryLoc:maskedValue})
    return memory


lines = []
with open("day14.txt","r")as a:
    lines = a.readlines()

memory = {}
data = []
oneMask = []

for l in range(len(lines)):
    if l == 0:     
        oneMask.append(lines[l])
    elif l == len(lines)-1:
        oneMask.append(lines[l])
        data.append(oneMask)
    elif "mask" in lines[l]:
        data.append(oneMask)
        oneMask = []
        oneMask.append(lines[l])
    else:
        oneMask.append(lines[l])

print(data)

res = {}
for d in data:
    r = runMemory(d,memory)
    res.update(r)

#sum = 0
#for r in res:
#    sum += int(res[r],2)
#print(sum)
