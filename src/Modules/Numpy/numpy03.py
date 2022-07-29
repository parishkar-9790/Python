# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
#   python class on numpy
# ...............................................................

import numpy as np
import pandas

if __name__ == '__main__':
    x=np.array([[2,3,3],[1,2,5]])
    print(x)
    y=np.np.swapaxes(x,0,1)
    print(y)
    z=np.array([[0,1][2,3][4,5][6,7]])
    print(z)
    z1=np.np.swapaxes(z,0,2)
    print(z1)
