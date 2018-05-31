from scipy.fftpack import fft, ifft

from numpy import array

a=array([2.3,3.1,4.2,-1.8,1.6,5.9])

print (a)

b = fft(a)

print(b)

b_inverse = ifft(a)

print(b_inverse)

a_sum = a.sum()

print(a_sum)