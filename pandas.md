       
---
Table
---
|   | Animal |
|---|:------:|
| 0 | Dog    |
| 3 | Cat    |
| 1 | wofl   |
| 2 | tiger  |
# 👆🏼 Table A


### Slicing
- `.iloc[]` takes only integers and similar to list slicing. 
  - `A.iloc[0:3]` return the whole table above. 


- `.loc[]` takes label only and slice based on given label values.
  - `A.loc['x':'y']` select everything between `x` and `y`. 
  - **CAUTION**: If labels are integer and not in-order then `iloc[]` and `loc[]` return different selection. 
- `.ix[]` 
