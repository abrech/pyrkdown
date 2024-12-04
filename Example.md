# This is an example file
Let's write some code!

The following code block will be executed and print statements will be append to this file:
```python
import matplotlib.pyplot as plt
for i in range(3):
  plt.plot([1 + i, 2, 3], [1, 4, 9 - i])
  plt.show()
print("hi")
plt.show()
```
> ### Output  
> hi  
> ![a plot](plot.png)

^ This was generated!  
Ideen:
- Zuweisungen suchen und dann im dict checken ob vorhanden, wenn variable einzeln in zeile
  - regex ist dann \n whitespaces varname(a-Z0-9_) whitespaces \n
- plots aufteilen? plt.clear() oder so?
