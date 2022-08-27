import numpy as np

def check(i):
    for j in range(no_r):
        if(needed[i][j]>available[j]):
            return 0
    return 1


no_p = 5
no_r = 4

Sequence = np.zeros((no_p,),dtype=int)
visited = np.zeros((no_p,),dtype=int)

allocated = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1]])
maximum = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2]])

needed = maximum - allocated
available = np.array([3,3,4])

count = 0
while( count < no_p ):
    temp=0
    for i in range( no_p ):
        if( visited[i] == 0 ):
            if(check(i)):
                Sequence[count]=i;
                count+=1
                visited[i]=1
                temp=1
                for j in range(no_r):
                    available[j] += allocated[i][j] 
    if(temp == 0):
        break


if(count < no_p):
    print('The system is Unsafe')
else:
    print("The system is Safe")
    print("Safe Sequence: ",Sequence)
    print("Available Resource:",available)