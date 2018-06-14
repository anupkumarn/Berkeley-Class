# Changing plot limits:
import pylab as plb 

plb.figure(figsize=(6,3), dpi=100)
d=plb.linspace(-plb.pi*2, plb.pi*2, 128, endpoint=True)
d_sin=plb.sin(d) 
d_cos=plb.cos(d) 

#setting the axis
ax1 = plb.gca() #gca - get current axis
ax1.spines['top'].set_color('none')  # to get rid of black border line
ax1.spines['bottom'].set_color('none')  # to get rid of black border line
ax1.spines['left'].set_color('none')  # to get rid of black border line
ax1.spines['right'].set_color('none')  # to get rid of black border line
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data',0))
ax1.spines['bottom'].set_color('gray')

