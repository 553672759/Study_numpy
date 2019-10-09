import numpy as np
import matplotlib.pyplot as plt
from pylab import *

#x = np.arange(0,3 * np.pi,0.00001)
#y = np.sin(x)
#y2 = np.cos(x)
#plt.title("Sin")
#plt.plot(x,y)
#plt.plot(x,y2,"y-")
#plt.show()
#散点图
n=10240
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
scatter(x,y)
show()