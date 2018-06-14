# Contour plot

import pylab as plb 

def f(x,y):
    return( 2 - x/3 + x**6 + 2.125*y) * plb.exp(-x**2 - y**2)

n = 128
x = plb.linspace(-2,2,n)
y = plb.linspace(-1,1,n)
A,B = plb.meshgrid(x,y)

plb.cla() 
plb.axes([0.075,0.075, 0.92,0.92])

plb.contourf(A, B, f(A,B), 12, alpha=0.50, cmap=plb.cm.gist_rainbow)
#plb.contourf(A, B, f(A,B), 12, alpha=0.50)#, cmap=plb.cm.gist_ncar)


C = plb.contour(A, B, f(A,B), 8, colors='black', linewidths=0.65)

plb.clabel(C, inline=1, fontsize=14)
plb.xticks(()); plb.yticks(())
#plb.pause(2) 
plb.show()
