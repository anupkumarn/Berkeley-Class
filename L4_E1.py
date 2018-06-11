from numpy import matrix, array, ndarray, int16, dot 

A = array([[2,3,4],[4,5,6]])

print(A) 

B = matrix([[2,3,4],[4,5,6]])

print(B) 
C = ndarray([2,3],dtype=int16)

print(C) 
C[0,:] = A[0,:]

print(C)
C[1,:] = B[1,:]
print(C)

A*A
B*B.T
C*C

dot(A,A.T)
dot(C,C.T)