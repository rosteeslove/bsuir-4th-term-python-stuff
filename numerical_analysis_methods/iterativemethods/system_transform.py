import numpy as np

# A:array-n-x-n * x:array-n-x-1 = b:array-n-x-1
# ->
# x:array-n-x-1 = B:array-n-x-n * x:array-n-x-1 + c:array-n-x-1
def system_transform(A: np.array, b: np.array):
    A = A.copy()
    c = b.copy()

    for i in range(len(A)):
        assert A[i, i] != 0
        c[i] /= A[i, i]
        A[i] /= A[i, i]

    B = np.identity(len(A)) - A

    return B, c
