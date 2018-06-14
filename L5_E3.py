import pylab as plb 

plb.figure(figsize=(10,6), dpi=120)

a=plb.linspace(-plb.pi*2, plb.pi*2, 512, endpoint=True)

b_sin, c_cos = plb.sin(a), plb.cos(a)

plb.subplot(2,1,1)

#different ways of plotting...gives same result
plb.plot(a,b_sin, color="red",linewidth=1.5, linestyle="-.")
plb.plot(a,b_sin, "r",linewidth=1.5, linestyle="-.")
plb.plot(a,b_sin, "-.r",linewidth=1.5)


plb.subplot(3,2,5)
plb.plot(a,c_cos, color="blue",linewidth=2.5, linestyle="--")

plb.show()