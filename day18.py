#%%
# PART 1
import re

def solve(p):
    numbers = re.findall("\d{1,}",p)
    operators = re.findall("\D",p)
    result = int(numbers[0])
    numbers.pop(0)
    for op in operators:
        if op == "+":
            result += int(numbers[0])
        elif op == "*":
            result *= int(numbers[0]) 
        else:
            print("error input: ",op)
            continue
        numbers.pop(0)
    return result


lines = open("day18.txt","r").readlines()

[l for l in lines]
finalSum = 0
print(lines[0].rfind("("))
for l in lines:
    toEvaluate = l.replace(" ","")
    lineSum = 0
    while toEvaluate.count("(") > 0:
        firstP = toEvaluate.rfind("(")+1
        closingP = toEvaluate.find(")",firstP)
        parenthesis = toEvaluate[firstP:closingP]
        result = solve(parenthesis)
        toEvaluate = toEvaluate[0:firstP-1] + str(result) + toEvaluate[closingP+1:]
    result = solve(toEvaluate)
    finalSum += result

print(finalSum)


#%%
# PART 2
import re

def solve(p):
    numbers = re.findall("\d{1,}",p)
    operators = re.findall("\D",p)

    while "+" in operators:
        ind = operators.index("+")
        rr = int(numbers[ind]) + int(numbers[ind+1])
        numbers[ind] = rr
        numbers.pop(ind+1)
        operators.pop(ind)

    while "*" in operators:
        rr = int(numbers[0]) * int(numbers[1])
        numbers[0] =  rr
        numbers.pop(1)
        operators.pop(operators.index("*"))

    return numbers[0]

lines = open("day18.txt","r").readlines()

finalSum = 0
print(lines[0].rfind("("))
for l in lines:
    toEvaluate = l.replace(" ","")
    lineSum = 0
    while toEvaluate.count("(") > 0:
        firstP = toEvaluate.rfind("(")+1
        closingP = toEvaluate.find(")",firstP)
        parenthesis = toEvaluate[firstP:closingP]
        result = solve(parenthesis)
        toEvaluate = toEvaluate[0:firstP-1] + str(result) + toEvaluate[closingP+1:]
    result = solve(toEvaluate)
    finalSum += result

print(finalSum)