## Image 2/2:
#import pylab as plb 
import matplotlib.image as img 
import matplotlib.pyplot as plt  

image = img.imread('L5_E4.png')
plt.imshow(image)
plt.pause(5)

luminosity = image[:,:,0]
plt.imshow(luminosity)
plt.pause(5)

plt.imshow(luminosity, cmap='hot')
plt.pause(5)
plt.imshow(luminosity, cmap='spectral')
plt.pause(5)

