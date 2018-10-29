import numpy as np
import matplotlib.pyplot as plt 
import math

#Factor n interpolator
def sinwave(n):
    x = [0]*n
    for i in range(n):
        angle = 2*math.pi*i/(n-1)
        x[i] = math.sin(angle)
    return x

if __name__ == "__main__":
    #n  = input()
    # n = 17
    yaxisval = []
    xaxisval = []
    for n in [13,17,20,26,30,34,36,40,46,50]:
        sinarray10 = sinwave(11)
        sinarrayn = sinwave(n+1)
        templist = [0]*(n+1)
        #print(sinarray10)
        
        for i in range(n+1):
            #print(i, i*10/n)
            #print(i, i*10/n)
            #print(math.ceil(i*10/n)-math.floor(i*10/n))
            if i == n or i == 0:
                templist[i] = 0
            elif math.ceil(i*10/n)-math.floor(i*10/n) == 0:
                #print(i*10/n)
                templist[i] = sinarray10[int(i*10/n)]
            else:    
                templist[i] = sinarray10[int(math.floor(i*10/n))] - (i*10/n - math.floor(i*10/n) )*((sinarray10[int(math.floor(i*10/n))]-sinarray10[int(math.ceil(i*10/n))])/(math.ceil(i*10/n)-math.floor(i*10/n)))
    
        sqlist = [math.pow(sinarrayn[:n][iter] - templist[:n][iter],2) for iter in range(len(sinarrayn[:n]))]
        yaxisval.append(sum(sqlist)/len(sqlist))
        xaxisval.append(n/10)
        print("MSE Error %d Samples:" % n,sum(sqlist)/len(sqlist))

    plt.title("MSE PLOT")
    plt.plot(xaxisval,yaxisval)
    # plt.stem(np.arange(n+1),templist[:n+1])

    plt.show()

    # templist30 = [math.pow(sinarray30[:30][iter] - y30[:30][iter],2) for iter in range(len(sinarray30[:30]))]
    # print("MSE Error 30 Samples:",sum(templist30)/len(templist30))

