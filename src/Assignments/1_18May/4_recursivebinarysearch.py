# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Binary Search recursive
# ...............................................................

def binarysearch(arr, start, end, key):
    if start < end:
        mid = int((start+end)/2)
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            return binarysearch(arr, start, mid, key)
        elif arr[mid] < key:
            return binarysearch(arr, mid+1, end, key)
    return False


if __name__ == '__main__':
    arr = [23, 50, 183, 219, 233, 345, 657, 696]
    key = int(input("Enter the key to search for : "))
    if binarysearch(arr, 0, len(arr), key):
        print("Key found")
    else:
        print("key not found  ")
