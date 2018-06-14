from numpy import matrix, array, random, min, max

A = random.random(15)
A = A.reshape(3,5)
A = matrix(A)

A.size
len(A)

A = A[0:3,0:4]

B = A.T 

B[:,1].min()

A.min()
A.max()

X = array([random.random(4)])

def function_HW2(a,b):
    return a*b.T
        
D = function_HW2(X,A)

Z=6+5j

Z.real
Z.imag
abs(Z)

C = D * abs(Z)

B = str(B)


