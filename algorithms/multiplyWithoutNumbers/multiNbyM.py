
multTable = []
for i in range(10):
    A = []
    for j in range(10):
        A.append(str(i*j))
    multTable.append(A)
    print(A)

addTable = []
for i in range(10):
    A = []
    for j in range(10):
        A.append(str(i+j))
    addTable.append(A)
    print(A)

def mod10(x):
    return x[-1]
def tenthDigit(x):
    if len(x) > 1:
        return x[0]
    return "0"
def add(x, y):
    result = ""
    carry = "0"
    for p in range(min(len(x), len(y))):
        i = x[-1-p]
        j = y[-1-p]
        sumOfTwo = addTable[int(i)][int(j)]
        if len(sumOfTwo) == 1:
            sumOfTwo = addTable[int(carry)][int(sumOfTwo)]
            carry = tenthDigit(sumOfTwo)
            sumOfTwo = mod10(sumOfTwo)
        else:
            temp = sumOfTwo[-1]
            temp = addTable[int(temp)][int(carry)]
            carry = addTable[int(tenthDigit(temp))][int(sumOfTwo[0])]
            sumOfTwo = temp
        result = sumOfTwo + result 
    for i in range(len(x), len(y)):
        d = y[-1-i]
        sumOfTwo = addTable[int(d)][int(carry)]
        carry = tenthDigit(sumOfTwo)
        sumOfTwo = mod10(sumOfTwo)
        result = sumOfTwo + result
    for i in range(len(y), len(x)):
        d = x[-1-i]
        sumOfTwo = addTable[int(d)][int(carry)]
        carry = tenthDigit(sumOfTwo)
        sumOfTwo = mod10(sumOfTwo)
        result = sumOfTwo + result
    if carry != "0":
        result = carry + result
    
    if result == "":
        return "0"
    
    return result
    

def multi(x, y):
    return multTable[int(x)][int(y)]
def singleAddition(x, y): 
    return addTable[int(x)][int(y)]
def addition(x, y):
    print(x, y)
    return addTable[int(x)][int(y)]

def multi1toN(x, y):
    #x is a single digit
    #y is a multi digit number
    if x == "0" or y == "0":
        return "0"
    if x == "1":
        return y
    if y == "1":
        return x
    result = ""
    carry = "0"
    for i in range(len(y)):
        d = y[-1-i]
        v = multTable[int(x)][int(d)]
        s = add(carry, v)
        result = mod10(s) + result
        carry = tenthDigit(s)
    if carry != "0":
        result = carry + result
    return result

def multiBy10(power, number):
    if number == "0":
        return "0"
    while power > 0:
        number = number +"0"
        power -= 1
    return number


def multiNbyN(x, y):
    if x == "0" or y == "0":
        return "0"
    if x == "1":
        return y
    if y == "1":
        return x
    result = "0"
    for i in range(len(x)):
        d = x[-1-i]
        multiplicationResult = multi1toN(d, y)
        multiplicationResult = multiBy10(i, multiplicationResult)
        result = add(result, multiplicationResult)
    return result    




import random
for i in range(100):
    x = random.randint(0,1000)
    y = random.randint(0, 1000)

    
    print(x*y, multiNbyN(str(x), str(y)))

  
