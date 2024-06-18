import numpy as np

L = [[1,2], [3,4]]
#print(L[0]) ... [1, 2]
#print(L[0][1]) ... 2

A = np.array([[1,2], [3,4]])
#print(A) ... [[1 2][3 4]]

#print(A[0][1]) ... 2
#print(A[0,1]) ... 2
#print(A[:,0]) ... array([1, 3])

A_Transpose = A.T
#print(A_Transpose)

A_Exp = np.exp(A)
#print(A_Exp) ... [[ 2.71828183  7.3890561 ][20.08553692 54.59815003]]

L_Exp = np.exp(L)
#You can pass lists through numpy to create numpy arrays directly

B = np.array([[1,2,3],[4,5,6]])

dot = A.dot(B)
#print(dot) ... [[ 9 12 15][19 26 33]]

det = np.linalg.det(A)
#print(det) ... -2.0000000000000004

inv = np.linalg.inv(A)
#print(inv) ... [[-2.   1. ][ 1.5 -0.5]]

identity = np.linalg.inv(A).dot(A)
#print(identity) ... [[1.00000000e+00 0.00000000e+00][1.11022302e-16 1.00000000e+00]]

trace = np.trace(A)
#print(trace) ... 5

diag = np.diag(A)
#print(diag) ... [1 4]

diag = np.diag([1, 4])
#print(diag) ... [[1 0][0 4]]

eigen = np.linalg.eig(A)
#print(eigen) ... ([-0.37228132,  5.37228132]), eigenvectors=array([[-0.82456484, -0.41597356],[ 0.56576746, -0.90937671]]))

Lam, V = np.linalg.eig(A)
check = V[:,0] * Lam[0] == A @ V[:,0]
#print(check) ... [ True False]
#precision error, use allclose
check = np.allclose(V[:,0] * Lam[0], A @ V[:,0])
#print(check) ... True