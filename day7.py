#%%
lines = []
with open("day7.txt","r") as a:
    lines = a.readlines()

def test(lines, gold):
    newLines = [] 
    golds = []
    
    if len(gold) != 1:
        for g in gold:
            golds.append(g)
    
    # Remove duplicates
    golds = list(dict.fromkeys(golds))

    for l in lines:
        lineContains = False
        bag,contains = l.split("bags contain")
        for g in gold:
            if contains.find(g) != -1:
                lineContains = True
                golds.append(bag)
        if lineContains == False:
            newLines.append(l)
    return newLines, golds

lin, gold = test(lines,["shiny gold"])
while True:
    temp = len(gold)
    lin, gold = test(lin,gold)
    print(len(gold),len(lin),len(lines))
    if temp == len(gold):
        break

print(len(gold))
# %%

#PART 2

lines = []
with open("day7.txt","r") as a:
    lines = a.readlines()

def test(lines, gold):
    golds = {}
    total = 1

    for l in lines:
        bag,contains = l.split("bags contain")
        for g in gold:
            if bag.find(g) != -1:
                golds.update(contains)
    return golds, total


bag = {}
total = 0
while True:
    if total == 0:
        bag,total = test(lines,{"shiny gold":1})  
        print(bag)
    else:
        bag,total = test(lines,bag)
    if len(bag) == 0:
        break

print(bag)
  

#%%



def mysplit(s):
    head = s[0:1]
    tail = s[len(head):].strip()
    return head, tail

def test(gold):
    lines = []
    with open("day7.txt","r") as a:
        lines = a.readlines()   

    #print("this is:",gold)
    total = 0
    for g in gold:
        amount, bag = mysplit(g)
        amount = int(amount)
        print("\nBag",amount,bag)
        if amount >= 1:
            total = total + int(amount)
        for l in lines:
            bags,contains = l.split("bags contain")
            if bags.find(bag) != -1:
                #print("Contains:",contains)
                newBags = contains.split(",")
                if newBags[0].find("no other bags") != -1:
                    print("Empty ",bag," Returning:",total)
                    return total
                else:
                    tem = 0
                    for bg in newBags:
                        rec = test([bg[0:bg.find("bag")].strip()])
                        total = amount * rec
                        tem = tem + total
                        #print(bg,"in",bag,amount,total)
                        #print("tem for",bag,tem)
                    tem = tem + amount                        
                print("returning:",bag,tem)
                return tem
    
# Output will be 1 greater than it should
test(["1 shiny gold"])-1



    
# %%
