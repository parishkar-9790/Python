# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# termwork 7
# ...............................................................
import numpy as np

if __name__ == '__main__':    
    num=np.loadtxt('X:\\Python\\src\\Termworks\\tw7.txt',delimiter=",", dtype=str)
    marks=num[:,1:4].astype(float)
    usn=num[:,4]
    avg=np.average(marks,axis=1)
    avg=np.round(avg)
    with open('X:\\Python\\src\\Termworks\\output.txt','w') as f:
        for i in range(len(usn)):
            f.write(usn[i]+" "+str(avg[i])+'\n')
        f.write(f'Higest Average is {round(np.max(avg),2)}')

            