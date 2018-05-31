from numpy import arange, sin
import matplotlib.pyplot as plt
x=arange(0.,20.,0.3)
y=sin(x)
ll = plt.plot(x,y)
plt.pause(4) # plt.show()