# Transformer
Python object transformation based on dictionary template
# Usage
```python

from transformer import Transformer

class Foo(object):
    def __init__(self):
        self.first_name = "Hassan"
        self.last_name = "Ali"
        self.age = 21
source = Foo()

template = {
            'name': '${first_name} + " " + ${last_name}',
            'years_old': '"%d years old" %${age}'
        }
t = Transformer(template)
t(source) # {'name': 'Hassan Ali', 'years_old': '21 years old'}
```

### Pass source as a dictionary ###
You can also pass source attribute as a dictionary 
```python
from transformer import Transformer

sourceDict = {
            "first_name": "Hassan",
            "last_name": "Ali",
            "age": 21
        }

template = {
            'name': '${first_name} + " " + ${last_name}',
            'years_old': '"%d years old" %${age}'
        }
t = Transformer(template)
t(sourceDict) # {'name': 'Hassan Ali', 'years_old': '21 years old'}
```
In the above code the sourceDict is a dictionary which contains the values to be substituted in the template

