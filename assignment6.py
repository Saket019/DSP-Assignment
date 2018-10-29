import numpy as np 
import cmath
import math

def DCT(x):
    N  = len(x)
    Y = [0]*2*N
    for k in range(2*N):
        for i in range(N):
            Y[k] += round(2*x[i]*math.cos(math.pi*k*(2*i+1)/(2*N)),2)
    return Y




if __name__ == "__main__":
    x = [8,]
    y = DCT(x)
    print("DCT :: " ,y)

