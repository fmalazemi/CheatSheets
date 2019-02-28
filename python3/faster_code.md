All based on Youtube Talk. Link
OS: 
Python 3 version:

## Timeit code


## Count elements in a list
Number of iterations 1.
Slow code: 
#### SLOW CODE:  
```python 
MILLION = [x for x in range(10**6)] #one time creation

how_many = 0
for element in MILLION:
  how_many += 1
print(how_many)
```
#### OUTPUT
```
0.05464205500175012 Seconds ( = 54.61 milli seconds)
```
#### FAST CODE:
```python
print(len(MILLION))
```
#### OUTPUT
```
3.492001269478351e-06 Seconds ( = 3.49 ns)
```

Speed up 
```
15717 times faster
```
