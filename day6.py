#%%

lines = []
with open("day6.txt","r") as a:
    lines = a.readlines()

lines.append("\n")
groups = []
group  = ""
for l in lines:
    if l == "\n":
        groups.append(group)
        group  = ""
        
    else:
        group  = group + l.strip()

total = 0
for g in groups:
    print(g)
    total = total + len("".join(set(g)))

print("part1: "+str(total))



#%%


lines = []
with open("day6.txt","r") as a:
    lines = a.readlines()

alp = "abcdefghijklmnopqrstuvwxyz"

lines.append("\n")
groups = []
group  = []
for l in lines:
    if l == "\n":
        groups.append(group)
        group  = []
        
    else:
        group.append(l.strip())

total = 0
for g in groups:
    res = 0
    answer = "".join(g)
    for a in alp:
        if answer.count(a) == len(g):
            res = res +1
    total = total +res

print(total)
    

