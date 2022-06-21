import os
import sys
import time
import numpy as np

l = range(1000)
a = np.array([1, 2, 3])
start = time.time()

# print(a)
# for i in l:
#     print(i)
# print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
for i in array:
    print(i)

# print(array.size*array.itemsize)
end = time.time()

print(end-start)
