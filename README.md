# HashableDict
A hashable immutable dictionary for Python. It lets you store dictionaries in sets or as keys to other dictionaries.
## Usage
```python
from HashableDict.HashableDict import HashDict

alive_list  = [("Ada Lovelace", False),
               ("Douglas Adams", False),
               ("Sylvia Plath", False),
               ("Alan Turing", False),
               ("you and your dreams", True)]

alive_dict = HashDict(alive_list)

if alive_dict["you and your dreams"]:
    print("The dream is alive!")

dict_within_dict = {alive_dict: None}
print(dict_within_dict)
```

## See also
- [FrozenDict](https://pypi.org/project/frozendict/)
