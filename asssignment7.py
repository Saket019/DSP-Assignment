import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import random


np.set_printoptions(suppress=True)

def DFT(x):
    N = len(x)
    D = np.ones((N,N),dtype = complex)
    for i in range(1,N):
        for k in range(1,N):
            D[i][k] = np.exp(-2j*(np.pi*i*k)/N)

    y = np.matmul(D,np.transpose(x))
    return np.transpose(y)

def IDFT(y):
    N = len(y)
    D = np.ones((N,N),dtype = complex)
    for i in range(1,N):
        for k in range(1,N):
            D[i][k] = np.exp(2j*(np.pi*i*k)/N)

    z = np.matmul(D/N,np.transpose(y))
    return np.transpose(z)

def DCT(x):
    N  = len(x)
    Y = np.array([0.]*N)
    for k in range(N):
        for i in range(N):
            Y[k] += 2.0*x[i]*math.cos(math.pi*k*(2.0*i+1)/(2.0*N))
    return Y

def IDCT(y):
    N  = len(y)
    Y = np.array([0.]*N)
    for i in range(N):
        for k in range(N):
            if k == 0:
                CONST = 0.5
            else:
                CONST = 1    
            Y[i] += CONST*y[k]*math.cos(math.pi*k*(2*i+1)/(2*N))
    return Y/N

h2 = np.array([[1,1],[1,-1]])/math.sqrt(2)

def haar_mat(n):
    n = int(n)
    if n == 1:
        return h2
    else:
        a = np.kron(haar_mat(n-1),[1,1])
        b = np.kron(np.identity(int(math.pow(2,n-1)))*math.pow(2,(n-1)/2.0),[1,-1])
        #print(np.concatenate((a,b),axis=0))
        return np.concatenate((a,b),axis=0)/math.sqrt(2)

def haar(x):
    return np.matmul(haar_mat(math.log(len(x),2)),np.transpose(x))
    

def inverse_haar(y):
    n = int(math.log(len(y),2))
    N = len(y)
    hn = haar_mat(n)
    return np.matmul(np.transpose(hn)/N,np.transpose(y))
     


def Edft(x,L):
    y = DFT(x)
    N = len(y)
    a = int((N+1-L)/2)
    b = int((N-1+L)/2)
    for i in range(a,b+1):
        y[i] = 0
    x_m = IDFT(y)

    return ((x - x_m) ** 2).mean(axis=0)

def Edct(x,L):
    y = DCT(x)
    N = len(y)
    for i in range(N-L,N):
        y[i] = 0
    x_m = IDCT(y)

    return ((x - x_m) ** 2).mean(axis=0)

def Ehaar(x,L):
    y = haar(x)
    N = len(y)
    for i in range(N-L,N):
        y[i] = 0
    x_m = inverse_haar(y)

    return ((x - x_m) ** 2).mean(axis=0)



if __name__=="__main__":
    X = np.array(random.sample(range(100),64))
    print("\nX: ", X)
    plt.figure()
    ydft = [0.]*64
    ydct = [0.]*64
    yhaar = [0.]*64
    for L in range(64):
        ydft[L] = Edft(X,L)
        ydct[L] = Edct(X,L)
        yhaar[L] = Ehaar(X,L) 
    plt.title('Energy Compaction Comparison Plot')
    plt.plot(range(64),ydft,'--b',label = "DFT")
    plt.plot(range(64),ydct,'-r',label = 'DCT')
    plt.plot(range(64),yhaar,'-g',label = 'Haar')
    plt.legend(loc='upper left')    
    plt.xlabel("L")
    plt.ylabel("E(L)")
    plt.show()
    

    # #DFT transform
    # x = [1,2,0,1]
    # y = DFT(x)
    # print(y)
    # print(IDFT(y))

    # #DCT Transform
    # x = [1,2,3,4]
    # y = DCT(x)
    # print(y)
    # print(IDCT(y))

    # #haar, transform
    # x = np.array([1,2,3,4])
    # output = np.matmul(haar(math.log(len(x),2)),np.transpose(x))
    # print(output)
    # y = output
    # output_inverse = np.matmul(inverse_haar(math.log(len(y),2),len(y)),np.transpose(y))
    # print(output_inverse)
