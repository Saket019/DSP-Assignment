import numpy as np
from __future__ import division

fig,ax = subplots()
f  = 1.0
fs = 5.0
t = arange(-1,1+1/fs,1/fs)
x= sin(2*pi*f*t)
ax.plot(t,x,"o-")