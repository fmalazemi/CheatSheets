from multiWithoutStringOfDigits import multiNbyN


import random
for i in range(100):
    x = random.randint(0,1000)
    y = random.randint(0, 1000)

    if(x*y !=  int(multiNbyN(str(x), str(y)))):
        print("Failed ", x*y, multiNbyN(str(x), str(y)))
    
