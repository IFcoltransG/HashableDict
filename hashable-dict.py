class HashableBox:
    '''
    A hashable container for storing unhashable things,
    Which compares equal to
    '''

    def __init__(self, contents=None):
        self.contents = contents

    def __repr__(self):
        return f"HashableBox({repr(self.contents)})"

    def __hash__(self):
        '''
        All boxes will have a hash collision.
        '''
        return hash(0)

    def __eq__(self, other):
        '''
        Checks if other is a HashableBox
        '''
        return isinstance(other, HashableBox)


class HashableFrozenDict:
    '''
    An immutable dictionary that is hashable, even if its values are not.
    '''

    def __init__(self, base_iterable=None, **kwargs):
        '''
        HashableFrozenDict() = empty dictionary
        HashableFrozenDict(iterable)
            = dictionary with keys made from pairs in iterable
        HashableFrozenDict(**kwargs) = dictionary made from kwargs
        '''
        if base_iterable is None:
            base_iterable = kwargs
        if isinstance(base_iterable, dict):
            base_iterable = base_iterable.items()
        contents = set()
        keys = set()
        for key, value in base_iterable:
            # wrap values in hashable boxes in case of mutability
            contents.add((key, HashableBox(value)))
            keys.add(key)
        self.__contents = frozenset(contents)
        self.__keys = frozenset(keys)

    def get(self, key_to_find, default=None):
        '''
        if key is in self, return self[key]
        otherwise, return default
        '''
        if key_to_find in self:
            return self[key_to_find]
        return default

    def items(self):
        '''
        Returns the (frozen-)set of (key, value) pairs
        '''
        boxed_key_val_pairs = self._get_contents()
        return frozenset((key, box.contents) for key, box in boxed_key_val_pairs)

    def keys(self):
        '''
        Returns the (frozen-)set of keys in the dictionary
        '''
        return self.__keys

    def __iter__(self):
        '''
        Iterate through the dictionary keys in an unspecified order
        '''
        yield from self.keys()

    def __repr__(self):
        '''
        Return a string representation in the form
        'HashableFrozenDict({key1: value1, key2: value2})'
        '''
        pairs = ((repr(key), repr(value)) for key, value in self.items())
        formatted_pairs = (f"{key}: {value}" for key, value in pairs)
        inner = ", ".join(formatted_pairs)
        return "HashableFrozenDict({" + inner + "})"

    def __eq__(self, other):
        '''
        Compares self to a dict or HashableFrozenDict
        by checking if all keys and values are the same
        '''
        if isinstance(other, dict):
            other = HashableFrozenDict(other)
        if not isinstance(other, HashableFrozenDict):
            return False
        return self._get_contents() == self._get_contents()

    def __hash__(self):
        '''
        Hashes using a frozenset of dict keys
        '''
        return hash(self.keys())

    def __contains__(self, key):
        '''
        Returns a boolean for if the key is in the dictionary
        '''
        return key in self.keys()

    def __getitem__(self, key_to_find):
        for key, value in self.items():
            if key == key_to_find:
                return value
        raise KeyError(key_to_find)

    @classmethod
    def fromkeys(cls, keys_iterable, value=None):
        '''
        Create a new dictionary with keys from iterable and values set to value.
        '''
        return HashableFrozenDict((key, value) for key in iterable)

    def _get_contents(self):
        '''
        Return the internal __contents frozenset
        (such as for checking equality)
        '''
        return self.__contents
