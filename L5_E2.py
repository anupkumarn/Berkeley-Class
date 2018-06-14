import numpy as np 
import matplotlib.pyplot as plt 

a=np.linspace(-np.pi*2, np.pi*2, 512, endpoint=True)

b_sin, c_cos = np.sin(a), np.cos(a)

plt.plot(a,b_sin)
plt.plot(a,c_cos)
#plt.bar(b_sin,c_cos)
#plt.pause(1)
plt.show()
