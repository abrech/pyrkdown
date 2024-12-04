# This is an example file
Let's write some code!

The following code block will be executed and print statements will be append to this file:
```python
from math import pi
def fnc():
    show = ""
    for i in range(5):
        show += str(i)
        if i > 2:
            print(show)
    print(pi)
fnc()
```
^ This was generated!  
Ideen:
- Zuweisungen suchen und dann im dict checken ob vorhanden, wenn variable einzeln in zeile
  - regex ist dann \n whitespaces varname(a-Z0-9_) whitespaces \n
