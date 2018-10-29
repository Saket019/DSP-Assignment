import numpy as np
import cmath
import math
def DFT(x):
    N = len(x)
    theta = 2*math.pi/N
    W = np.exp(-2j*math.pi/N)
    #print(W**2)
    # print(W)
    # temp = [complex(0,0)]*N
    # print(temp)
    D = np.ones((N,N),dtype = complex)
    #print(D)
    for i in range(1,N):
        for k in range(1,N):
            #print(i,k)
            D[i][k] = np.exp(-2j*(np.pi*i*k)/N)
            #print(np.matrix(D))
    #print(np.matrix(D))
    y = np.matmul(x,D)
    return y

if __name__ == "__main__":
    x = [1,2,0,1]
    print(x)
    print(DFT(x))
