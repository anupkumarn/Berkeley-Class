import pylab as plb 

r = plb.array([2,40,60,80,100])
print(r)
print(r[:,plb.newaxis].shape)
print(r[plb.newaxis,:].shape)
s = r - r[:,plb.newaxis]
print(s)

plb.figure('Testing broadcasting', dpi=65)
plb.gca(title = 'Testing broadcasting')
