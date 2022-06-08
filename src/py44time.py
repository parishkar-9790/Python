# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Time modules
# ...............................................................
import time

start = time.time()

for i in range(10000):
    print("Print")
print(time.time()-start)
