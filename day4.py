#%%
line = []
with open("day4.txt", "r") as a:
    line = a.readlines()

passes = [x for x in line]
fp = []
pas = ""

for p in passes[]:
    if p != "\n":
        pas = pas + p
    else:
        fp.append(pas)
        pas = ""

correctPass = 0

cr = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

for p in fp:
    isTrue = True
    for c in cr:
        if  c not in p:
            isTrue = False
        
    if isTrue == True:
        correctPass = correctPass +1

print(correctPass)

#%%

import re

def makePassports(dataI):
    passports = []
    onePass = ""
    for p in dataI:
        if p != "\n":
            onePass = onePass + p
        else:
            passports.append(onePass)
            onePass = ""
    return passports

line = []
with open("day4.txt", "r") as a:
    line = a.readlines()

passports = makePassports(line)
requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
eyeC = ["amb","blu","brn","gry","grn","hzl","oth"]

correct = 0
for f in passports:
    isTrue = True
    for reqField in requiredFields:
        if  reqField not in f:
            isTrue = False
    
    if isTrue == True:
        byr = int(f[f.find("byr:")+4:f.find("byr:")+8].strip())
        iyr = int(f[f.find("iyr:")+4:f.find("iyr:")+8].strip())
        eyr = int(f[f.find("eyr:")+4:f.find("eyr:")+8])
        hgt = f[f.find("hgt:")+4:f.find("hgt:")+8]
        hgt = int(re.findall(r'\d+',hgt)[0])
        inch = "in" in f[f.find("hgt:")+4:f.find("hgt:")+10]
        cm = "cm" in f[f.find("hgt:")+4:f.find("hgt:")+10]
        hcl = f[f.find("hcl:#")+5:f.find("hcl:#")+11]
        h = ""
        try:
            he = int(hcl,16) #is hexadecimal
        except:
            h
        else:
            h = hcl 
        ecl =  f[f.find("ecl:")+4:f.find("ecl:")+8]
        pid = f[f.find("pid:")+4:f.find("pid")+13]
        if byr < 1920 or byr > 2002:
            isTrue = False
        if iyr < 2010 or iyr > 2020:
            isTrue = False
        if eyr < 2020 or eyr > 2030:
            isTrue = False
        if cm == True: 
            if hgt < 150 or hgt > 193:
                isTrue = False
        if inch == True:
            if hgt < 59 or hgt > 76:
                isTrue = False
        if inch == False and cm == False:
            isTrue = False
        if len(h) != 6:
            isTrue = False
        eye = False

        for c in eyeC:
            if c in ecl:
                eye = True
        if eye == False:
            isTrue = False
        
        if len(pid) != 9:
            isTrue = False
        if pid.isdigit() == False:
            isTrue = False

        if isTrue == True:
            correct = correct +1

print(correct)

