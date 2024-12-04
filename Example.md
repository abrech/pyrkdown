# This is an example file
Let's write some code!

The following code block will be executed and print statements will be append to this file:
```python
from math import pi

show = ""
for i in range(5):
    show += str(i)
print(show)
print(pi)
```
> 01234  
3.141592653589793


^ This was generated!
Ideen:
- Zuweisungen suchen und dann im dict checken ob vorhanden, wenn variable einzeln in zeile
  - regex ist dann \n whitespaces varname(a-Z0-9_) whitespaces \n
`