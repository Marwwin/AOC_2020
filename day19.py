#%%
import re
import numpy as np

def checkCode(code,rules):
    isCode = checkRule(code,rules[0])

def checkRule(code,rule):
    print(rule)
    isRuleTrue = True
    for r in rule:
        isRT = True
        if type(r) == int:
            checkRule(code,rulesInt[r])
        #checkRule()
    #checkRule(code,rulesInt[rule[0]])

#%%
rulesInt[120]

#%%

lines = open("day19.txt","r").readlines()

rules = [re.findall("\d.*",l) for l in lines]
rules = list(filter(None,rules))
rules = [r[0].split() for r in rules]
rulesInt = {}
for r in rules:
    r[0] = r[0][:-1]
    ruleInt = []
    for elem in r: 
        try:
            elem = int(elem)
        except:
            elem = elem
        ruleInt.append(elem)
    rulesInt.update({ruleInt[0]:ruleInt[1:]})
    ruleInt = []

rules.sort()

codes = [re.findall("[a-z].*",l) for l in lines]
codes = list(filter(None,codes))[2:]

for c in codes[0]:
    checkCode(c,rulesInt)

