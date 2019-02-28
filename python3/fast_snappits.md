Below are several performance benchmarks between different implementations for the same task in Python 3 (version 3.6.1). Most of the snappits are extracted from the [Youtube lecture by Sebastian Witowski](https://www.youtube.com/watch?v=YjHsOrOOSuI&t=611s). 

1. [Count elements in a list](###Count elements in a list)




### Timeit code





### Count elements in a list
#### SETUP CODE
```python
MILLION_CELL_LIST = [x for x in range(10**6)]
```
#### SLOW CODE:  
```python 
how_many = 0
for element in MILLION_CELL_LIST:
  how_many += 1
print(how_many)
```
#### FAST CODE:
```python
print(len(MILLION_CELL_LIST))
```
##### RESULTS: 
```
SLOW CODE = 54.61 milli seconds
FAST CODE = 3.49 ns
15717 times speedup. 
```
---
### Fliter List
#### SETUP CODE:
```python
MILLION_CELL_LIST = [x for x in range(10**6)]
```
#### SLOW CODE 1:
```python 
output = []
for element in MILLION:
	if element % 2 == 0:
		output.append(element)
```
#### SLOW CODE 2:
```python 
list(filter(lambda x : x % 2, MILLION))
```
#### FAST CODE:
```python
[item for item in MILLION if item %2] 
```
#### RESULTS:
```
SLOW CODE 1 :  96.78  mi.
SLOW CODE 2 : 146.65  mi.
FAST CODE   :  58.088 mi.
SPEEDUP     : 1.71 times
```

---

### Permission or Forgiveness 1
If your code will rarely raise an expecetion try-except will be faster. 

### SETUP CODE:
```python
class FOO:
	hello = 'hello'
foo = FOO()
```
#### SLOW CODE:
```python
if hasattr(foo, 'hello'):
	foo.hello
```
#### FAST CODE:
```python
try:
	foo.hello
except AttributeError:
	pass
```
#### RESULTS:
```
SLOW CODE : 2.166 ms.
FAST CODE : 0.822 ms.
2.09 times speedup
```


### Permission or Forgiveness 2
If your code will raise an expecetion most of the time, try-except will be slower. 

### SETUP CODE:
```python
class FOO:
	pass 
foo = FOO()
```
#### SLOW CODE:
```python
try:
	foo.hello
except AttributeError:
	pass
```
#### FAST CODE:
```python
if hasattr(foo, 'hello'):
	foo.hello
```
#### RESULTS:
```
SLOW CODE : 613.49 ms.
FAST CODE : 470.57 ms.
SPEEDUP   : 1.3 times.
```

### Membership testing

#### SETUP CODE:
```python
MILLION = [x for x in range(10**6)] 
number = 500000
def check_member(number):
	for item in MILLION:
		if item == number:
			return True
	return False
```
#### SLOW CODE:
```python
check_member(number)	
```
#### FAST CODE:
```python 
number in MILLION
```
#### RESULTS: 
```
SLOW CODE : 17.60 milliseconds.
FAST CODE :  8.86 milliseconds.
SPEEDUP   :  1.98 times. 
```
---

### `float()` vs `*1.0`
Using function float to convert an int to float will require calling the function `float()` and then execute it. However, multiplying by `1.0` avoid loading any function and directly apply multiplication op. Check assembly code for both. 

#### SETUP CODE:
```python
pass

```
#### SLOW CODE:
```python
def float_func(n):
	return float(n)
```
`dis.dis(float_func)` output
```nasm
0 LOAD_GLOBAL              0 (float)
2 LOAD_FAST                0 (n)
4 CALL_FUNCTION            1
6 RETURN_VALUE
```

#### FAST CODE:
```python 
def mul_by_float(n):
	return n * 1.0
```
`dis.dis(mul_by_float)` output
```nasm
0 LOAD_FAST                0 (n)
2 LOAD_CONST               1 (1.0)
4 BINARY_MULTIPLY
6 RETURN_VALUE
```
#### RESULTS: 
```
SLOW CODE: 147.16 ns.
FAST CODE: 15.77 ns.
SPEEDUP  : 9.33 times.
```

## Remove Duplicates

#### SETUP
```python
import random
L = [random.randint(1,10000) for x in range(10**4)] 
```

#### SLOW CODE:
```python
unique = []
for e in L:
	if e not in unique:
		unique.append(e)
```
#### FAST CODE:
```python
unique = set(L)
```
#### RESULTS:
```
SLOW CODE : 491.692 milliseconds
FAST CODE :   0.751 milliseconds
Speedup: 654 times
```
---
### Sorting
Both codes are the same except CODE_1 has an overhead of creating a new list. 
If we repeat this benchmark we will notice a slowness in CODE_1 due to creating a new list. 
#### SETUP:
```python
import random
MILLION = [random.randint(1,100000) for x in range(10**6)] 
```

#### CODE_1:
```python
sorted(MILLION)
```

#### CODE_2:
```python
MILLION.sort()
```
#### RESULTS:
```
CODE_1 : 621.48 milliseconds
CODE_2 : 621.25 milliseconds
SPEEDUP: 0 
```
---
### Checking for True
In the `FAST_CODE` we dont need to compare `b` with `True`, so it need less number of instructions. 
#### SETUP:
```python
b = True
```

#### SLOW_CODE_1:
```python
if b == True:
	pass
```
#### SLOW_CODE_2:
```python
if b is True:
	pass
```
#### FAST_CODE:
```python
if b:
	pass
```
#### RESULTS
```
SLOW_CODE_1 : 934.99 ns
SLOW_CODE_2 : 544.00 ns
FAST_CODE   : 385.99 ns
SPEEDUP     : 2.42 times from SLOW_CODE_1 to FAST_CODE
```
---

### `list()` or `[]`, `dict()` or `{}`
Using `list()` will force to load the function and then build it. Alternatively, `[]` can directly build a list. 
#### SLOW_CODE:
```python
list()
```
#### FAST_CODE:
```python
[]
```
#### RESULTS:
```
SLOW_CODE : 1423 ns.
FAST CODE : 496  ns.
SPEEDUP   : 2.86 times. 
```













