# Map, Fliter, Reduce

## map(func, iterables)
Apply func to the given iterable(s) and return an iterator. The number of iterables depends on func parameters. 
`def square(x):
    return x**2
lst = [1,2,3,4]
sq_lst = list(map(square, lst))
print(sq_lst)

sq_lst2 = list(map(lambda x : x**2, lst))
print(sq_lst2)`
