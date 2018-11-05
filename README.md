# Ormuco tests

All tests were made using Python 3.7 (conda virtual env) and default libraries.


# Question A

A program that accepts two lines (x1, x2) and (x3, x4) on the x-asis and returns whether they overlap. 
Return True if overlap.


## Usage

```bash
python question_a.py -l1 <x1> <x2> -l2 <x3> <x4>
```

# Question B

A software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other.
This test was done based on question example ("1.1", "1.2") and it's not validating any string with more than one point.
To compare indexes it's necessary use other python functions like `zip` to ordenate and compare.   

## Usage
```bash
python question_b.py <str1> <str>
```
## Examples
```bash
python queston_b.py '2.1' '2.1'
2.1 == 2.1
python queston_b.py '1.2' '2.1'
1.2 < 2.1
python queston_b.py '3.9' '3.2'
3.9 > 3.2
```

## Testing
```bash
python tests_question_b.py
```

# Question C

A Geo Distributed LRU cache with time expiration.

## Install

```bash
git clone https://github.com/lepri/ormuco_tests/
cd ormuco_tests
pip install -e question_c
```

## Usage

Let's use the LRUCache to cache the pages accessed by users. `app` it's an app that uses Ormuco LRUCache.

```python
from cache import CacheItem, LRUCache
from app.utils import get_requests, get_data

cache = LRUCache(size=1024, expires=600 , region='Toronto')

# get the user data from request
user = get_request()

if user in cache:
    url = cache.get(user)
else:
    url = get_data(user)
    user = Data(user, url)
    cache.set(user)

# return cache item to user
serve_result(url)

# remove expired content
cache.remove_expired()

```

## Testing

```bash
python test_question_c.py
```