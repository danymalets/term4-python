import numpy as np

n = 5

C = np.array([
    [0.2,   0, 0.2,   0, 0.2],
    [  0, 0.2,   0, 0.2,   0],
    [0.2,   0, 0.2,   0, 0.2],
    [  0, 0.2,   0, 0.2,   0],
    [0.2,   0, 0.2,   0, 0.2]
], dtype=np.float64)

D = np.array([
    [ 2.33,  0.81,  0.67,  0.92, -0.53],
    [-0.53,  2.33,  0.81,  0.67,  0.92],
    [ 0.92, -0.53,  2.33,  0.81,  0.67],
    [ 0.67,  0.92, -0.53,  2.33,  0.81],
    [ 0.81,  0.67,  0.92, -0.53,  2.33],
], dtype=np.float64)

Q = np.empty((n, n), dtype=np.float64)

k = 5

A = C * k + D

b = np.array([4.2, 4.2, 4.2, 4.2, 4.2], dtype=np.float64)

x = np.empty(n, dtype=np.float64)

for i in range(n):
    s = ''
    for j in range(n):
        s += str(round(A[i][j], 2)) + ' * x' + str(j + 1)
        if j != n - 1:
            s += ' + '
    s += ' = ' + str(b[i])
    print(s)
print()

for row in range(n - 1):
    ind_max = row
    for i in range(row + 1, n):
        if abs(A[i][row]) > abs(A[ind_max][row]):
            ind_max = i
    (A[row], A[ind_max]) = (A[ind_max], A[row])
    b[row], b[ind_max] = b[ind_max], b[row]
    for i in range(row + 1, n):
        q = A[i][row] / A[row][row]
        A[i] -= q * A[row]
        b[i] -= q * b[row]

for row in range(n - 1, -1, -1):
    column = n - 1 - row
    for j in range(row + 1, n):
        b[row] -= x[j] * A[row][j]
    x[row] = b[row] / A[row][row]

for i in range(n):
    print('x' + str(i + 1), '=', round(x[i], 4))