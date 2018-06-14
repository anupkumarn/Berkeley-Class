## Image 1/2:
import pylab as plb 

plb.cla() 

array= plb.random((80,120))

plb.imshow(array, cmap=plb.cm.gist_rainbow) # with a specific colormap
plb.pause(5)