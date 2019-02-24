# Map, Fliter, Reduce

## map(func, iterables)
Apply func to the given iterable(s) and return an iterator. The number of iterables depends on func parameters. 
`map` is a built-in function. 
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
## filter(func, iterable)
For a given boolean function func and an iterable, create a list of elements e1, e2, ..., en such that func(ei) == true. 
Filter return an iterator of the created list. 
`filter` is a built-in function. 
```python
def isOdd(x):
    return x % 2 != 0
lst = list( range(11) )
print(lst)
odd_lst = list( filter(isOdd, lst))
print(odd_lst)
even_lst = list( filter(lambda x : x % 2 == 0, lst))
print(even_lst)
```
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]
[0, 2, 4, 6, 8, 10]
```
## reduce(func, iterable)
Perform computation on the iterable and return a single element (not iterable.) 
For a given list `lst = [1,2,3,4]` and `func(x,y)` that returns the sum `x+y`, `reduce` will roll the computation as `reduce(func, lst) = func(func(func(1, 2), 3), 4) = 10`
`reduce` is not a built-in function it is part of `functools`. 
```python
from functools import reduce
lst = list(range(1, 10))
result = reduce((lambda x, y: x * y), )
print(result)
```
```
362880
```



