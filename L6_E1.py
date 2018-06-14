## Advanced plotting:
# Bar plot:
import pylab as plb 

for i in range(5):
    k = 8
    x = plb.arange(k)
    y1 = plb.rand(k) * (1 - x / k)
    y2 = plb.rand(k) * (1 - x / k)

    plb.axes([0.075, 0.075, 0.88, 0.88])

    plb.bar(x, +y1, facecolor='#9922aa', edgecolor = 'green')
    plb.bar(x, -y2, facecolor='#ff3366', edgecolor = 'green')

    for a, b in zip(x,y1):
        plb.text(a+0.11, b+0.08, '%.3f' % b, ha='center', va='bottom')
    for a, b in zip(x,y2):
        plb.text(a+0.11, -b-0.08, '%.3f' % b, ha='center', va='top')

    plb.xlim(-.5,k), plb.ylim(-1.12, +1.12)
    plb.grid(True)
#    plb.show()
    plb.pause(1)    # plb.pause already implements plb.show.
    plb.cla()



