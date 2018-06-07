from scipy import poly1d

x = poly1d([4,2,6])

print (x)

print (x*x)

print(x.integ(k=5))

print (x.deriv())