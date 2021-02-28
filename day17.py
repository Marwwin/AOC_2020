#%%
lines = []

with open("day17.txt","r") as a:
    lines = a.readlines()

dimensions = {(0,0,0):[l.strip() for l in lines]}

for cycle in range(6):
    
