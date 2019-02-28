All based on Youtube Talk. Link
OS: 
Python 3 version:

## Timeit code


## Count elements in a list
Number of iterations 1. 
```python 
MILLION = [x for x in range(10**6)] #one time creation

how_many = 0
for element in MILLION:
  how_many += 1
print(how_many)
```
```
0.05464205500175012 Seconds 54.64205500175012 mi
```
