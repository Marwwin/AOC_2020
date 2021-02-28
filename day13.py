#%%
import re

lines = []

with open("day13.txt","r") as a:
    lines = a.readlines()

timeStamp = int(lines[0].split()[0])

departures = lines[1]
busses = re.findall("\d{1,}",departures)
result = [{int(b)-(timeStamp%int(b)):int(b)} for b in busses]
res = {}
for r in result:
    res.update(r)
res[min(res.keys())]*min(res.keys())
#print(result.key())

#%%
import re

lines = []

with open("day13.txt","r") as a:
    lines = a.readlines()

departures = lines[1]
busses = re.findall("\d{1,}",departures)
departures = departures.split(",")
busses = [int(x) for x in busses]
largest = max(busses)
counter = 1
busses
#while True:
#    isT = True
#    for x in range(len(departures)):
#        if departures[x] != "x":
#            if (largest * counter) % int(departures[x]) != 0:
#                isT = False
#                break
#    counter += 1
#    if (counter % 100000000 == 0):
#        print(counter)
#    if isT:
#        break
#        print(largest * counter,isT)
#        
# %%
