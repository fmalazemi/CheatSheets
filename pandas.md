       
        |   | Animal|
        |---|-------|
Table A | 0 | Dog   |
        | 2 | Cat   |
        | 1 | camel |



### Slicing
- `.iloc[]` takes only integers and similar to list slicing. 
  - `A.iloc[x:y]` select everything between `x` and `y-1`. 


- `.loc[]` takes label only and slice based on given label values.
  - `A.loc['x':'y']` select everything between `x` and `y`. 
  - **CAUTION**: If labels are integer and not in-order then `iloc[]` and `loc[]` return different selection. 
- `.ix[]` 
