### 👇🏼 Table A
|   | Animal |
|---|--------|
| 0 | Dog    |
| 3 | Cat    |
| 1 | wofl   |
| 2 | tiger  |



### Slicing
- `.iloc[]` takes only integers and similar to list slicing. 
  - `A.iloc[0:3]` return the whole A.
- `.loc[]` takes label only and slice based on given label values.
  - `A.loc[0:3]` return first two rows. NOT the whole A. 
  - **CAUTION**: If labels are integers and not in-order then `iloc[]` and `loc[]` give different outputs. 
