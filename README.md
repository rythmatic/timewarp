# Timewarp
Timewarp is a simple python module that offers one functionality: measure 
execution time of functions.

## Installation
```
pip install git+https://github.com/rythmatic/timewarp
```

## Example Usage
```python
from timewarp import Timewarp

@Timewarp
def multiply(x, y):
    return x*y

multiply(12, 14)
```
```
multiply ran in 9.5367431640625e-07s
```

Or alternatively: 
```python
def multiply(x, y):
    return x*y

multiply = Timewarp(multiply)
multiply(12, 14)
```
```
multiply ran in 9.5367431640625e-07s
```

