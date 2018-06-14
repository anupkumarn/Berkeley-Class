import pylab as plb 

plb.figure(figsize=(10,6), dpi=120)

a=plb.linspace(-plb.pi*2, plb.pi*2, 512, endpoint=True)
b_sin, c_cos = plb.sin(a), plb.cos(a)

plb.subplot(2,1,1)
plb.plot(a,b_sin, color="red",linewidth=1.5, linestyle="-.")

plb.subplot(3,2,5)
plb.plot(a,c_cos, color="blue",linewidth=2.5, linestyle="--")

#plb.show()

plb.xlim(-8.0,8.0)

plb.xticks(plb.linspace(-8,8,6,endpoint=True))

plb.ylim(-1.2,1.4)

plb.yticks(plb.linspace(-1.2,1.4,4,endpoint=True))

plb.savefig("L5_E4.png", dpi=64)

plb.show()