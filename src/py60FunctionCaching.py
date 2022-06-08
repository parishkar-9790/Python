# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# function caching
# ...............................................................

import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(4)

    return f"The work is {n}"


if __name__ == '__main__':
    print('now running some work')
    print(some_work(1))
    print(some_work(3))
    print(some_work(7))
    print(some_work(9))
    print('done')
    print(some_work(3))
    print(some_work(7))
    print(some_work(9))
    print('calling again')
