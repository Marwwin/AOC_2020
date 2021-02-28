#%%

import re
import numpy as np

lines = open("day16.txt","r").readlines()

[l for l in lines[0:20]]

rules = lines[0:20]
yourTicket = lines[22]
yourTicket = re.findall("\d{1,}",yourTicket)
yourTicket = [int(x) for x in yourTicket]
tickets = lines[25:]

s = set()

for r in rules:
    nums = re.findall("\d{1,}",r)
    for i in range(int(nums[0]),int(nums[1])+1):
        s.add(i)
    for i in range(int(nums[2]),int(nums[3])+1):
        s.add(i)

result = 0
validTickets = []
for t in tickets:
    falseTicket = False
    nums = re.findall("\d{1,}",t)
    nums = [int(x) for x in nums]
    for n in nums:
        n = int(n)
        if n not in s:
            result += n
            falseTicket = True
    if not falseTicket:
        validTickets.append(nums)

print("part 1:",result)

#part2
testR = ["class: 0-1 or 4-19"
,"row: 0-5 or 8-19"
,"seat: 0-13 or 16-19"]
testNTicket = ["nearby tickets:",
"3,9,18",
"15,1,5",
"5,14,9"]

rulesList = []
names = []
for r in rules:
    nums = re.findall("\d{1,}",r)
    name = re.search(".*:",r)
    newSet = set()
    for i in range(int(nums[0]),int(nums[1])+1):
        newSet.add(int(i))
    for i in range(int(nums[2]),int(nums[3])+1):
        newSet.add(int(i))

    #names.append(name.group())
    #rulesSets.append(newSet)
    rulesList.append((name.group(),newSet))

end = []
validTicketsNp = np.array(validTickets)
for n in range(len(validTicketsNp[0])):
    column = np.unique(validTicketsNp[:,n])
    for r in range(len(rulesList)):
        ist = True
        for c in column:
            if c not in rulesList[r][1]:
                ist = False
                continue
        if ist:
            end.append((r,n))

# Count how many hits
zer = [0 for i in range(0,20)]
for e in end:
    zer[e[1]] += 1

# Get indexes of different elements
indexes = []
for z in range(1,len(zer)+1):
    print(zer.index(z))
    indexes.append(zer.index(z))

# Get sometingh
ress = []
for i in indexes:
    for e in end:
        if e[1] == i:
            if e[0] not in ress:
                ress.append(e[0])

finalRes = 1
res = []
for x in range(len(ress)):
    if "departure" in rulesList[ress[x]][0]:
        finalRes *= yourTicket[indexes[x]]

print(finalRes)
#%%
rules
