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
