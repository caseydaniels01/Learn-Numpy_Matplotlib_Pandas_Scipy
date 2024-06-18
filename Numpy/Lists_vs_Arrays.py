import numpy as np

L = [1, 2, 3]
A = np.array([1,2,3])

#for e in L:
#    print(e)

#for e in A:
#    print(e)

L.append(4)

#A.append(4)
#error - no append in numpy

L = L + [5]
#print(L) ... [1, 2, 3, 4, 5]

A = A + np.array([4])
#print(A) ... [5 6 7]

A = 2 * A
#print(A) ... [10 12 14]

L = 2 * L
#print(L) ... [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

L = [1, 2, 3]
L2 = []

for e in L:
    L2.append(e+3)

#print(L2) ... [4, 5, 6]

L = [1, 2, 3]
L2 = []

for e in L:
    L2.append(e**2)

#print(L2) ... [1, 4, 9]

A**2
#print(A) ... [10 12 14]

A = np.sqrt(A)
#print(A) ... [3.16227766 3.46410162 3.74165739]

A = np.log(A)
#print(A) ... [1.15129255 1.24245332 1.31952866]

A = np.exp(A)
#print(A) ... [3.16227766 3.46410162 3.74165739]

A = np.tanh(A)
#print(A) ... [0.99642288 0.9980424  0.99887585]