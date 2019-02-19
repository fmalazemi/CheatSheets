### Slicing
- `.iloc[]` takes only integers and similar to list slicing. 
  - `A.iloc[x:y]` select everything between `x` and `y-1`. 

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

- `.loc[]` takes label only and slice based on given label values.
  - `A.loc['x':'y']` select everything between `x` and `y`. 
  - **CAUTION**: If labels are integer and not in-order then `iloc[]` and `loc[]` return different selection. 
- `.ix[]` 
