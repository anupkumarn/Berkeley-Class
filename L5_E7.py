# Changing plot limits:
import pylab as plb 
plb.figure(figsize=(6,3), dpi=100)
d=plb.linspace(-plb.pi*2, plb.pi*2, 128, endpoint=True)
d_sin=plb.sin(d) 
d_cos=plb.cos(d)  

#we now set the x,y limits for the 'sin' function
plb.subplot(2,1,1)
plb.plot(d,d_sin, color="blue", linewidth=1.2, linestyle="-", label="sin")
plb.legend(loc="upper right")
plb.xlim(d_sin.min()*6.5, d_sin.max()*6.5)
plb.ylim(d_sin.min()*1.2, d_sin.max()*1.2)
plb.xticks([-plb.pi*2, -plb.pi, 0, plb.pi, plb.pi*2],
           ['$-2\pi$', '$-\pi$', '$0$','$+\pi$', '$+2\pi$'])
plb.yticks([-1,0,1],
           ['$-1$','$0$','$+1$'])
plb.title('Plot of Sin and Cos functions')

#below we set the x,y limits for the 'cos' function
plb.subplot(2,1,2)
plb.plot(d,d_cos, color="red", linewidth=1, linestyle="--", label="cos")
plb.legend(loc='lower right')
plb.xlim(d_cos.min()*6.5, d_cos.max()*6.5)
plb.ylim(d_cos.min()*1.2, d_cos.max()*1.2)

plb.interactive(True)
plb.pause(10)
plb.show()
