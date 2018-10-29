import numpy as np
import math
import matplotlib.pyplot as plt
#Factor 2 Interpolator
def sinwave(n):
    x = [0]*n
    for i in range(n):
        angle = 2*math.pi*i/(n-1)
        x[i] = math.sin(angle)
    return x

if __name__ == "__main__":
    sinarray = sinwave(101)
    sinarray10 = sinwave(11)
    sinarray20 = sinwave(21)
    sinarray30 = sinwave(31)

    #Factor 2 : Linear Interpolator
    xu = [0]*(2*len(sinarray10))
    for i,val in enumerate(sinarray10):
        xu[2*i] = val
    y = [0]*len(xu)
    for j,val in enumerate(xu):
        if j-1 < 0:
            y[j] = xu[j] + 0.5*(xu[j+1])
        elif j+1 == len(xu):
            y[j] = xu[j] + 0.5*(xu[j-1])
        else:
            y[j] =xu[j] + 0.5*(xu[j-1]+xu[j+1])
    
    plt.subplot(2,1,1)
    plt.title("interpolated samples")
    plt.plot(np.arange(21),sinarray20)
    plt.stem(np.arange(21),y[:21])



    templist = [math.pow(sinarray20[:20][iter] - y[:20][iter],2)for iter in range(len(sinarray20[:20]))]
    print("MSE Error 20 Samples:",sum(templist)/len(templist))

    #Factor 3

    xu30 = [0]*(3*len(sinarray10))
    for i,val in enumerate(sinarray10):
        xu30[3*i] = val
    #print(xu30)
    y30 = [0]*len(xu30)
    #print(len(xu30))
    for j,val in enumerate(xu30):
        #print(j)
        if j-1 == -1:
            y30[j] = xu30[j] + 2*(xu30[j+1])/3 +(xu30[j+2])/3
        elif j-2 == -1:
            y30[j] = xu30[j] + 2*(xu30[j-1]+ xu30[j+1])/3 +(xu30[j+2])/3
        elif j+1 == len(xu30):
            y30[j] = xu30[j] + 2*(xu30[j-1])/3 +(xu30[j-2])/3
        elif j+2 == len(xu30) :
            y30[j] = xu30[j] + 2*(xu30[j-1]+ xu30[j+1])/3 +(xu30[j-2])/3
        else:
            y30[j] = xu30[j] + 2*(xu30[j-1]+ xu30[j+1])/3 +(xu30[j-2]+xu30[j+2])/3

    plt.subplot(2,1,2)
    plt.title("30 samples")
    plt.plot(np.arange(31),sinarray30)
    plt.stem(np.arange(31),y30[:31])

    templist30 = [math.pow(sinarray30[:30][iter] - y30[:30][iter],2) for iter in range(len(sinarray30[:30]))]
    print("MSE Error 30 Samples:",sum(templist30)/len(templist30))


    plt.show()
"""
xu = [0]*(2*len(x))
for index,val in enumerate(x):
    xu[index*2] = val

y = [0]*len(xu)
for index,i in enumerate(xu):
    y[index] = 
"""