# Linear sum assignment, also known as minimum weight matching in bipartite graphs
# s.t. each row is assignment to at most one column, and each column to at most one row 


import numpy as np
cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])

from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost)

print(row_ind, col_ind)
print(cost[row_ind, col_ind].sum())