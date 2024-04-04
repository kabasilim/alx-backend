# alx-backend

## 0x01-caching

#### Base file
```
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Caching Systems
This repository contains Python scripts implementing various caching systems:

0. Basic Dictionary
### Description
- Implements a basic caching system without any limits.
- Inherits from ``BaseCaching``.
- Provides ``put`` and ``get`` methods for adding and retrieving items from the cache.
### Usage
```
from 0-basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
print(my_cache.get("A"))  # Output: Hello
print(my_cache.get("B"))  # Output: World
print(my_cache.get("C"))  # Output: Holberton
print(my_cache.get("D"))  # Output: None
```

1. FIFO Caching
### Description
- Implements a caching system using the First-In-First-Out (FIFO) algorithm.
- Inherits from ``BaseCaching``.
- Provides ``put`` and ``get`` methods.
- Discards the oldest item if the cache limit is reached.
### Usage
```
from 1-fifo_cache import FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
print(my_cache.get("A"))  # Output: Hello
my_cache.put("E", "Battery")
```

2. LIFO Caching
### Description
- Implements a caching system using the Last-In-First-Out (LIFO) algorithm.
- Inherits from ``BaseCaching``.
- Provides ``put`` and ``get`` methods.
- Discards the most recent item if the cache limit is reached.
### Usage
```
from 2-lifo_cache import LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
print(my_cache.get("A"))  # Output: Hello
my_cache.put("E", "Battery")
```

3. LRU Caching
### Description
- Implements a caching system using the Least Recently Used (LRU) algorithm.
- Inherits from ``BaseCaching``.
- Provides ``put`` and ``get`` methods.
- Discards the least recently used item if the cache limit is reached.
### Usage
```
from 3-lru_cache import LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
print(my_cache.get("B"))  # Output: World
my_cache.put("E", "Battery")
```


4. MRU Caching
### Description
- Implements a caching system using the Most Recently Used (MRU) algorithm.
- Inherits from ``BaseCaching``.
- Provides ``put`` and ``get`` methods.
- Discards the most recently used item if the cache limit is reached.
### Usage
```
from 4-mru_cache import MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
print(my_cache.get("B"))  # Output: World
my_cache.put("E", "Battery")
```


5. LFU Caching
### Description
- Implements a caching system using the Least Frequently Used (LFU) algorithm.
- Inherits from ``BaseCaching``.
- Provides ``put`` and ``get`` methods.
- Discards the least frequently used item if the cache limit is reached.
### Usage
```
from 100-lfu_cache import LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
print(my_cache.get("B"))  # Output: World
my_cache.put("E", "Battery")
```

