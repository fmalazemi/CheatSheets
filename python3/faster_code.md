All based on Youtube Talk. Link
OS: 
Python 3 version:

## Timeit code


## Count elements in a list
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
## Fliter List
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
SLOW CODE 1 : 0.096 seconds (= 96.78 mi.)
SLOW CODE 2 : 0.146 seconds (=146.65 mi.)
FAST CODE   : 0.058 seconds (= 58.088 mi.)
71% speedup from SLOW CODE 1 (1.71 speedup.) 
```

---

## Permission or Forgiveness 1
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
SLOW CODE : 1.46e-06 seconds (= 2.166 ms.)
FAST CODE : 6.95e-07 seconds (= 0.822 ms.)
2.09 times speedup
```


## Permission or Forgiveness 2
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
SLOW CODE : 6.134e-07 seconds (= 613.49 ns.)
FAST CODE : 4.705e-07 seconds (= 470.57 ms.)
30% speedup
```

## Membership testing

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
0.0176 seconds (=17.60 Milliseconds.)
0.0088 seconds (= 8.86 Milliseconds.)
1.98 speedup. 
```
---

## `float()` vs `*1.0`
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
SLOW CODE: 147.16 ns
FAST CODE: 15.77 ns
9.33 times speedup
```


