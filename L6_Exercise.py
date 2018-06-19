# Lecture 6, Class exercise
import pylab as plb 
from numpy import random 

A = {'k1':'', 'k2':'', 'k3':'', 'k4':'', 'k5':''}

def fn1(dict):
    for key, val in dict.items():
        val = random.randint(0,10)
    return dict

def fn2(dict):
    for key, val in dict.items():
        if val < 5:
            # 4.1 Using normal distrib. with mean=2 and std = 3 create a 256pts array
            val = plb.normal(loc=2, scale=3, size=256)
            # 4.2 Using a histogram with 12 bins, plot the result from 4.1
            #plb.figure("Histogram"), plb.title("Gaussian distribution histogram")
            #plb.hist(y[key])
            #colour='red', label='Normal')
    return dict

B = fn1(A)

C = fn2(B)

A['k1'] = A.pop('k2')
print(A)

A['k6'] = '124'
print(A)

A.pop('k5')
print(A)

# Check if A , B and C are equal
print('Check if A, B and C are equal: ', A is B is C)


