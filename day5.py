#%%
import itertools
# PART 1
lines = []
with open("day5.txt","r") as a:
    lines = a.readlines()
#max([ int(l[0:7].replace("B","1").replace("F","0"),2) * 8 + int(l[7:10].replace("L","0").replace("R","1"),2) for l in lines])

# Easier
max([int(l.replace("F","0").replace("L","0").replace("B","1").replace("R","1").strip(),2) for l in lines])

ss = {int(l.replace("F","0").replace("L","0").replace("B","1").replace("R","1").strip(),2) for l in lines}

res = itertools.accumulate(max(ss).difference(min(ss)))

#%%
# Part 2
lines = []
with open("day5.txt","r") as a:
    lines = a.readlines()

tickets = [[int(l[0:7].replace("B","1").replace("F","0"),2), int(l[7:10].replace("L","0").replace("R","1"),2)]  for l in lines]
sortedList = []
for i in range(0,127):
    row = []
    for x in tickets:
        if x[0] == i:
            row.append(x)
    sortedList.append(row)

sortedList = list(filter(None,sortedList))

res = 0
for x in sortedList:
    if len(x) != 8:
        seats = [s[1] for s in x]
        missing = [x for x in range(0,7) if x not in seats]
        if len(missing)==1:
            res = x[0][0] * 8 + missing[0]
            print(res)

# %%
