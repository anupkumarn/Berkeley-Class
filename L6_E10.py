# 3-D plot:
import pylab as plb 
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(plb.figure())
x = plb.arange(-3,3,0.35)
y = plb.arange(-4, 6, 0.35)
x, y = plb.meshgrid(x,y)
k = plb.sqrt(x**2 + y**2)
z = plb.sin(k)

ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plb.cm.gist_rainbow_r)
ax.contourf(x, y, z, zdir='z', offset=-3, cmap=plb.cm.gist_stern)
ax.set_zlim(-4,4)

plb.show()
