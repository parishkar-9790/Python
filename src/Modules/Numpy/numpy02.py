import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([2, 4, 7, 8, 9])
print(a1+a2)
# float ,dtype=np.complex

a3 = np.array([[1, 2], [3, 4], [5, 6]])
a4 = np.array([[5, 2], [7, 4], [9, 6]])
a = np.arange(1, 5)
# print(a3.ndim)// show the dimensions of the matrix 
# print(a3.size)// show the size of the array 
# print(a3.shape)//show the shape of the array 
# print(a3) // print the array 
# print(a3.dtype)
# print(a3.itemsize) // show the size of per element ie float , int 
print(a3.reshape(2, 3))
print(a3)
print(a3.ravel())
print(a.min())
print(a.max())
print(a.sum())
print(np.sqrt(a))
print(a.sum(axis=0))
# print(np.linspace(1, 5, 10))
print(a)
# hey there this is parishkar singh 
# this is numpy 
