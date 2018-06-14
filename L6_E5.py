# Histogram 1/2:
import pylab as plb 

plb.figure(1)
gaus_dist = plb.normal(-2,2,size=512)  # create a random floating point vector

#plot the histogrm with specific  bin number
plb.hist(gaus_dist, normed=True, bins=24) # default: bins=10 , coloue ='blue'

plb.title("Gaussian distribution /  Histogram")
plb.xlabel("value")
plb.ylabel("Frequency")
plb.grid(True)
plb.pause(5)