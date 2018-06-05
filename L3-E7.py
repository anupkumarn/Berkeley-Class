from numpy import arange
import time

N = int(input('Please Enter a number: '))

x = arange(N)
y = range(N)

tic = time.clock()
x.sum()
toc = time.clock()
t_numpy = toc - tic

tic = time.clock()
sum(y)
toc = time.clock()
t_list = toc - tic

print("numpy: %.3e sec" % (t_numpy))
print("list: %.3e sec" % (t_list))
print("diff: %.3e sec" % (t_list - t_numpy))
#print("numpy: %.3e sec" % (t_numpy))
