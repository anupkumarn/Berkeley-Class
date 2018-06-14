# Histogram 2/2:
import pylab as plb 

plb.figure(2)

gaus_dist = plb.normal(size=512)  # create a random floating point vector
unif_dist = plb.uniform(-5,5,size=512) # Create a uniform distribution vector

#plot the histogrm with specific  bin number, color, transparency, label
plb.hist(unif_dist, bins=24, histtype='stepfilled', density=True, color='cyan', label='Uniform') 
plb.hist(gaus_dist, bins=24, histtype='stepfilled', density=True, color='orange', label='Gaussian', alpha=0.65) 

plb.legend(loc='upper left')
plb.title("Gaussian vs Uniform distribution /  Histogram")
plb.xlabel("value")
plb.ylabel("Frequency")
plb.grid(True)
plb.pause(5)
