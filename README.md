# alx-backend

Pagination Helper Functions
This repository contains helper functions and classes for pagination tasks.

0. Simple Helper Function
### Description
This module provides a simple helper function called index_range that takes two integer arguments: page and page_size. The function returns a tuple containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Note that page numbers are 1-indexed, meaning the first page is page 1.

### Usage
```
from 0-simple_helper_function import index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
```


1. Simple Pagination
### Description
This module contains a class called Server, which facilitates pagination of a dataset of popular baby names stored in a CSV file. It includes a method get_page that retrieves a specific page of the dataset based on provided page number and page size.

### Usage
```
from 1-simple_pagination import Server

server = Server()

# Examples of retrieving dataset pages
print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
```


2. Hypermedia Pagination
### Description
Similar to the previous module, this module also contains a Server class but with an additional method get_hyper for hypermedia pagination. This method returns a dictionary containing pagination metadata along with the dataset page.

### Usage
```
from 2-hypermedia_pagination import Server

server = Server()

# Examples of retrieving dataset pages with hypermedia pagination
print(server.get_hyper(1, 2))
print(server.get_hyper(2, 2))
print(server.get_hyper(100, 3))
print(server.get_hyper(3000, 100))
```


3. Deletion-Resilient Hypermedia Pagination
### Description
This module extends the hypermedia pagination concept to handle cases where rows may be removed from the dataset between queries. It introduces a method get_hyper_index that takes into account potential deletions and ensures consistency in pagination.

### Usage
```
from 3-hypermedia_del_pagination import Server

server = Server()

# Examples of retrieval with deletion-resilient hypermedia pagination
print(server.get_hyper_index(3, 2))
```
