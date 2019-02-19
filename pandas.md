### Slicing
- `.iloc[]` takes only integers and similar to list slicing. 
  - `A.iloc[x:y]` select everything between `x` and `y-1`. 
- `loc[]` takes label only and slice based on given label values.
  - `A.loc['x':'y']` select everything between `x` and `y`. 
  - **CAUTION**: If labels were integers, `iloc[]` and `loc[]` may return different selection for the same selection string.  
