# Polar plot:
import pylab as plb 

plb.axes([0.065,0.065,0.88,0.88], polar = True)

q = 24
t = plb.arange(0.015, 3*plb.pi, 3*plb.pi/q)
rad = 12 * plb.rand(q)
w = plb.pi / 4 * plb.rand(q)
ba = plb.bar(t, rad, width = w)

for r , bar in zip(rad, ba):
    bar.set_facecolor(plb.cm.jet(r/12.0))
    bar.set_alpha(0.75)

plb.show()


