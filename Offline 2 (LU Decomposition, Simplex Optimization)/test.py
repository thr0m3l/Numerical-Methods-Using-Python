import numpy as np

def simplex(c, A, b):
    table = initialize(c, A, b)
    while not search_optimum(table):
        pass
    return solution(c, table)
def initialize(c, A, b):
    (m, n), k = A.shape, len(c)
    # simplex table:
    # |A|E|b|
    # |c|0|0|
    table = np.zeros((m + 1, m + n + 1))
    table[:m, :n] = A
    table[range(m), range(n, n + m)] = 1
    table[:-1, -1] = b
    table[-1, :k] = c
    return table
def search_optimum(table):
    index = np.argwhere(table[-1, :-1] > 0).ravel()
    
    # optimum found
    if not len(index):
        return True
    
    # pivotal column
    j = index[0]
    column = table[:-1, j].copy()
    column[column <= 0] = -1
    
    if np.all(column <= 0):
        raise ArithmeticError('the system is unbounded')
    # pivotal row
    pivots = table[:-1, -1] / column
    pivots[column <= 0] = np.inf
    i = np.argmin(pivots).ravel()[0]
    # eliminate by pivot at (i, j)
    row = table[i] / table[i][j]
    table[:] -= np.outer(table[:, j], row)
    table[i, :] = row
    table[:, j] = table[:, j].round()
def solution(c, table):
    (m, n), k = table.shape, len(c)
    # pivotal columns
    s = np.sum(table == 0, axis=0) == m - 1
    t = np.sum(table == 1, axis=0) == 1
    # solution
    x = np.zeros(n - 1)
    for j in range(n - 1):
        if s[j] and t[j]:
            x[j] = table[:, j] @ table[:, -1]
    return dict(
        x=x[:k],
        slack=x[k:],
        max=-table[-1, -1],
        table=table,
    )