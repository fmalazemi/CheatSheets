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
#### FAST CODE:
```python
print(len(MILLION))
```
##### Speed up 
```
15717 times faster 
Slow = 54.61 milli seconds
Fast = = 3.49 ns
```
