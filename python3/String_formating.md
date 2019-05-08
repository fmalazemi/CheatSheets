# String formatting


### 1. The very old way ```%```:
  ```python3
    Name = "Aristotle"
    print("Knowing yourself is the beginning of all wisdom -- %s "% Name)
  ```

### 2. The Not very old way ```format```:
    ```python3
      firstName = "Albert"
      lastName = "Einstein"
      print("Any fool can know. The point is to understand.-- {} {}".format(firstName, lastName))
    ```
### 3. The New Way is the ```f``` string:
    ```python
      firstName = "Albert"
      lastName = "Einstein"
      print(f'Weak people revenge. Strong people forgive. Intelligent people ignore. -- {firstName} {lastName}')
    ```
   * Add  leading spaces to an integer:
   ```python3
   for i in range(3):
     print(f'The i value is {i:4}')
   i = 999
   print(f'No leading in this case {i:2}')
   ```
   OUTPUT:
   ```
   The i value is    0
   The i value is    1
   The i value is    2
   No leading in this case 999
   ```
   * You may replace space with ```0``` as:
   ```python3
   for i in range(3):
     print(f'The i value is {i:04}')
   i = 999
   print(f'No leading in this case {i:02}')
   ```
   OUTPUT:
   ```
   The i value is 0000
   The i value is 0001
   The i value is 0002
   No leading in this case 999
   ```
   * Floats formating:
   ```python3
   pi = 3.141592653589793
   print(f'Show only 4 digits after decimal point -> {pi:.4f}')
   print(f'Show 0 digits after decimal point -> {pi:.0f}')
   ```
   OUTPUT
   ```
   Show only 4 digits after decimal point -> 3.1416
   Show 0 digits after decimal point -> 3
   ```
   
   
   
   
