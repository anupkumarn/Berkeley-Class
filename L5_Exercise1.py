#Name: Anup Kumar
from numpy import matrix, array, random, min, max 
import pylab as plb 

A = random.random_sample(600)

B = plb.linspace(-plb.pi*3, plb.pi*2, 500, endpoint=True)

def replace_elem(arr):
    #print("Array min/max :", arr.min()," - ", arr.max())
    #for i, k in enumerate(arr, start = 0) :
    for i in range(arr.size):
        if arr[i] < 2 or arr[i] > 9:
                arr[i] = (arr.min() + arr.max()) /2
#                print(arr[i])
                arr[i] = (arr[i] / ( arr.max() / 0.1 ))
#                print(arr[i])
                
C = replace_elem(A)
#print(C)

C = array(C)
#print(C)

D = C[0:len(B)] + B

