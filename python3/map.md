# Map, Fliter, Reduce

## map(func, iterables)
Apply func to the given iterable(s) and return an iterator. The number of iterables depends on func parameters. 
```python
def square(x):
    return x**2
lst = [1,2,3,4]
sq_lst = list(map(square, lst))
print(sq_lst)

sq_lst2 = list(map(lambda x : x**2, lst))
print(sq_lst2)
```
```
[1, 4, 9, 16]
[1, 4, 9, 16] 
```
Function with more than one parameter. 
```python
lst = [1,2,3]
lst2 = [4,5,6]
result = list(map(lambda x,y : x+y, lst, lst2))
print(result)
```
```
[5, 7, 9]
```

Apply map to a list of functions.

```python
def mul(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [mul, add]
for i in range(3):
    result = list(map(lambda x: x(i), funcs))
    print(result)
```
```
[0, 0]
[1, 2]
[4, 4]
```
## filter(func, iterables)
For a given boolean function func and iterables, create a list of elements e1, e2, ..., en such that func(ei) == true. 
Filter return an iterator of the created list. 
```
def isOdd(x):
    return x % 2 != 0
lst = [x for x in range(11)]
print(lst)
result = list( filter(isOdd, lst))
print(result)
```
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]
```
