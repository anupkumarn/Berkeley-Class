## Scatter plot:

import pylab as plb 

x = plb.rand(1,2,1500)
print(x)
y = plb.rand(1,2,1500)
plb.axes([0.075,0.075,0.88,0.88])

plb.cla()
plb.scatter(x, y, s=65, alpha = .75, linewidth=0.125, c=plb.arctan2(x,y))

plb.grid(True)
plb.xlim(-0.085,1.085), plb.ylim(-0.085, 1.085)
#plb.pause(1)
plb.show()
